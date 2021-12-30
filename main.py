'''Instantiate and start a trading bot.'''

import json
import bots
import exchanges

file = open('authentication.json', 'r', encoding='UTF-8')
authentication = json.load(file)
file.close()
print(authentication)

'''
exchange = exchanges.abstract_exchange.Exchange('', '', '')
bot = bots.abstract_bot.Bot(exchange)

bot.start()
'''
