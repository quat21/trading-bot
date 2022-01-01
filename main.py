'''
Start a trading bot.

    Parameters:
        bot_name
        exchange_name
'''

import os
import logging
import json
import datetime
import importlib
from helper import Interval, Side, TimeInForce
from exchanges.abstract_exchange import AbstractExchange
from bots.abstract_bot import AbstractBot


def get_credentials(exchange: str) -> dict:
    '''Return authentcation data for a given exchange.'''
    file = open('authentication.json', 'r', encoding='UTF-8')
    authentication = json.load(file)
    file.close()
    if exchange in authentication.keys():
        return authentication[exchange]
    return {}


def purge_logs() -> None:
    '''Delete all logs.'''
    files = [file for file in os.listdir('logs') if file.endswith('.log')]
    for file in files:
        os.remove(os.path.join('logs', file))


def prepare_logger(bot_name, exchange_name):
    '''Prepare the logger.'''
    current_time = datetime.datetime.today()
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s-%(levelname)s-%(message)s',
        filename=f'logs/{bot_name}-{exchange_name}-{current_time}.log',
        filemode='w',
    )


def initialize_exchange(exchange_name: str) -> AbstractExchange:
    '''Try to initialize the exchange and terminate if something fails.'''
    credentials = get_credentials(exchange_name)
    try:
        exchange_module = importlib.import_module(f'exchanges.{exchange_name}')
    except ModuleNotFoundError as exception:
        logging.error('no code found for the exchange "%s"', exchange_name)
        raise exception
    try:
        return exchange_module.Exchange(credentials['key'],
                                        credentials['secret'],
                                        credentials['password'])
    except AttributeError as exception:
        logging.error(
            'no Exchange class found for the exchange "%s"', exchange_name)
        raise exception


def initialize_bot(bot_name: str, exchange: AbstractExchange) -> AbstractBot:
    '''Try to initialize the bot and terminate if something fails'''
    try:
        bot_module = importlib.import_module(f'bots.{bot_name}')
    except ModuleNotFoundError as exception:
        logging.error('no code found for the bot "%s"', bot_name)
        raise exception
    try:
        return bot_module.Bot(exchange)
    except AttributeError as exception:
        logging.error('no Bot class found for the bot "%s"', bot_name)
        raise exception


def start_bot(bot_name: str, exchange_name: str) -> None:
    '''Start a trading bot.'''
    purge_logs()
    prepare_logger(bot_name, exchange_name)
    exchange = initialize_exchange(exchange_name)
    bot = initialize_bot(bot_name, exchange)
    bot.start()


if __name__ == '__main__':
    # start_bot('abstract_bot', 'coinbase_sandbox')
    exchange = initialize_exchange('coinbase_sandbox')
    if False:
        print(exchange.get_price('btc-usd'))
        print(exchange.get_price_history(
            'btc-usd',
            datetime.date(2021, 1, 20),
            datetime.date(2021, 1, 21),
            Interval.MIN
        ))
    print(exchange.place_limit_order(
        'btc-usd',
        Side.BUY,
        10000,
        0.0001,
        TimeInForce.GTC
    ))
