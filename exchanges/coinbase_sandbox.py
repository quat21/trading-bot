'''Interface for the coinbase sandbox exchange.'''

import logging
from typing import List
import datetime
import calendar
import json
import time
import requests
from helper import Interval, Side, TimeInForce
# from exchanges.abstract_exchange import AbstractExchange


class Exchange():
    '''Interface for the coinbase sandbox exchange.'''

    def __init__(self,
                 key: str,
                 secret: str,
                 password: str):
        self.name = 'coinbase_sandbox'
        self.url = 'https://api-public.sandbox.exchange.coinbase.com'
        self.key = key
        self.secret = secret
        self.password = password

    def get_price(self, ticker_symbol: str) -> float:
        url = self.url + '/products/' + ticker_symbol + '/ticker'
        headers = {"Accept": "application/json"}
        try:
            response = requests.request('get', url, headers=headers).json()
            if response.get('message') is not None:
                logging.error('unknown ticker symbol in get_price')
                output = -1.0
            else:
                output = response['price']
        except requests.exceptions.ConnectionError:
            logging.error('connection error in get_price')
            output = -1.0
        return output

    def get_price_history(self,
                          ticker_symbol: str,
                          start_time: datetime.datetime = None,
                          end_time: datetime.datetime = None,
                          interval: Interval = None) -> List[list]:
        url = f'{self.url}/products/{ticker_symbol}/candles'
        params = {'granularity': self.convert_interval(interval)}
        if start_time is not None and end_time is not None:
            params['start_time'] = calendar.timegm(start_time.timetuple())
            params['end_time'] = calendar.timegm(end_time.timetuple())
        headers = {"Accept": "application/json"}
        try:
            response = requests.request(
                'get', url, params=params, headers=headers).json()
            if not isinstance(response, list):
                logging.error('issue with parameters in get_price_history')
                output = []
            else:
                output = self.format_candle_data(response)
        except requests.exceptions.ConnectionError:
            logging.error('connection error in get_price')
            output = []
        return output

    def convert_interval(self, interval: Interval) -> str:
        '''
        Convert from an Interval instance to a granularity parameter in the
        format required by the coinbase API.

        Default to '60' if the input is invalid.
        '''
        if interval == Interval.MIN:
            return '60'
        elif interval == Interval.FIVEMIN:
            return '300'
        elif interval == Interval.FIFTEENMIN:
            return '900'
        elif interval == Interval.HOUR:
            return '3600'
        elif interval == Interval.DAY:
            return '86400'
        else:
            return '60'

    def format_candle_data(self, candle_data: List[list]) -> List[list]:
        '''
        Change the format of candle data from get_price_history to the
        required format.
        '''
        for i in range(len(candle_data)):
            candle_data[i][0] = datetime.datetime.utcfromtimestamp(
                candle_data[i][0])

            temp = candle_data[i][1]
            candle_data[i][1] = candle_data[i][3]
            candle_data[i][3] = temp

            temp = candle_data[i][2]
            candle_data[i][2] = candle_data[i][4]
            candle_data[i][4] = temp
        return candle_data

    def place_limit_order(self,
                          ticker_symbol: str,
                          side: Side,
                          price: float,
                          size: float,
                          time_in_force: TimeInForce) -> str:
        url = f'{self.url}/orders'
        headers = self.auth_header
        params = {
            'profile_id': 'default profile_id',
            'product_id': ticker_symbol,
            'type': 'limit',
            'side': self.convert_side(side),
            'stp': 'dc',
            'time_in_force': self.convert_time_in_force(time_in_force),
            'price': str(price),
            'size': str(size)
        }
        try:
            response = requests.request(
                'post', url, json=params, headers=headers).json()
            print(response)
            if response.get('message') is not None:
                if response['message'] == 'Invalid API Key':
                    logging.error('Invalid API Key')
                output = ''
            else:
                output = response
        except requests.exceptions.ConnectionError:
            logging.error('connection error in place_limit_order')
            output = ''
        return output

    def convert_side(self, side: Side) -> str:
        '''
        Convert a Side Enum to a string for the Coinbase API.

        Default to 'sell'.
        '''
        if side == Side.BUY:
            return 'buy'
        else:
            return 'sell'

    def convert_time_in_force(self, time_in_force: TimeInForce) -> str:
        '''
        Convert a TimeInForce Enum to a string for the Coinbase API.

        Defulat to FOK.
        '''
        if time_in_force == TimeInForce.GTC:
            return 'GTC'
        elif time_in_force == TimeInForce.IOC:
            return 'IOC'
        else:
            return 'FOK'

    def sign_api_call(self, method: str, request_path: str, body: dict) -> str:
        '''
        Sign an API call for the Coinbase API.

        Create a base64 encoded sha256 HMAC using the base64-decoded secret key
        on the string timestamp + method + request_path + body.
        '''
        timestamp = str(time.time())
        body = str(body)
        message = timestamp + method + request_path + body
        header = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'cb-access-key': self.key,
            'cb-access-passphrase': self.password,
            'cb-access-sign': self.secret,
            'cb-access-timestamp': timestamp,
        }
        return header
