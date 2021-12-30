'''
Define an abstract Exchange class that defines the interface for an exchange.
'''

from abc import ABC, abstractmethod
from typing import List
import datetime
from helper import Interval, OrderInfo, Status, TimeInForce


class AbstractExchange(ABC):
    '''Interface for any exchange connection.'''

    def __init__(self,
                 key: str,
                 secret: str,
                 password: str):
        '''Initialize exchange connection.'''
        self.key = key
        self.secret = secret
        self.password = password
        self.status = Status.STARTING

    @property
    @abstractmethod
    def name(self):
        '''name of exchange'''

    @abstractmethod
    def get_price(self, ticker_symbol: str) -> float:
        '''Return the current price for a given ticker symbol.'''

    @abstractmethod
    def get_price_history(self,
                          ticker_symbol: str,
                          start_time: datetime.datetime,
                          end_time: datetime.datetime,
                          interval: Interval) -> List[list]:
        '''
        Return the price history for a given start time, end time, and
        interval.

        Output format: [[datetime.datetime, open, high, low, close, volume]]

        Note: Output is a list of klines/candlesticks. Volume is a float of the
        volume in the given ticker symbol.
        '''

    @abstractmethod
    def place_limit_order(self,
                          ticker_symbol: str,
                          price: float,
                          size: float,
                          time_in_force: TimeInForce) -> str:
        '''Submit a new order with the given parameters and return its id.'''

    @abstractmethod
    def cancel_order(self, order_id: str) -> bool:
        '''Cancel an order and return True if it was successful.'''

    @abstractmethod
    def cancel_all_orders(self) -> bool:
        '''Cancel all orders and return True if it was successful.'''

    @abstractmethod
    def get_order_info(self, order_id: str) -> OrderInfo:
        '''Return an OrderInfo object for a given order.'''

    @abstractmethod
    def get_all_open_orders(self) -> List[OrderInfo]:
        '''Return a list of OrderInfo objects for all orders.'''

    @abstractmethod
    def stop(self) -> None:
        '''Run cleanup processes and close exchange connection.'''
