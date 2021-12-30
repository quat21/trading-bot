'''Gives information on the exchanges module.'''

import pkgutil

EXCHANGES = [value.name for value in pkgutil.iter_modules(['exchanges'])]
EXCHANGES.remove('info')
EXCHANGES.remove('abstract_exchange')
