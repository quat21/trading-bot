'''Instantiate and start a trading bot.'''

import logging
import json
import bots
import exchanges


def get_authentication_data(exchange: str) -> dict:
    '''Return authentcation data for a given exchange.'''
    file = open('authentication.json', 'r', encoding='UTF-8')
    authentication = json.load(file)
    file.close()
    if exchange in authentication.keys():
        return authentication[exchange]
    else:
        return {}


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    filename='app.log',
    filemode='w',
)

authentication = get_authentication_data('coinbase_pro_sandbox')
exchange = exchanges.abstract_exchange.Exchange(authentication['key'],
                                                authentication['secret'],
                                                authentication['password'])
bot = bots.abstract_bot.Bot(exchange)

bot.start()
