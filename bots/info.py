'''Gives information on the bots module.'''

import pkgutil

TRADING_BOTS = [value.name for value in pkgutil.iter_modules(['bots'])]
TRADING_BOTS.remove('info')
TRADING_BOTS.remove('abstract_bot')
