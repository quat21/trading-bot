'''
Define required classes for modelling an action that a trading strateg
could take.
'''

from enum import Enum, auto
import dataclasses


class TimeInForce(Enum):
    '''Define possible times in force for an order.'''
    GTC = auto()
    IOC = auto()
    FOK = auto()


class Status(Enum):
    '''Define possible status values for an exchange or bot.'''
    STARTING = 'starting'
    STOPPING = 'stopping'
    ACTIVE = 'active'
    ERROR = 'error'


class Interval(Enum):
    '''Define all possible intervals for kline/candlestick data.'''
    MIN = auto()
    FIVEMIN = auto()
    FIFTEENMIN = auto()
    HOUR = auto()
    DAY = auto()


@dataclasses.dataclass
class OrderInfo:
    '''Contain all relevant information for an order.'''
    order_id: str
    ticker_symbol: str
    price: float
    size: float
    time_in_force: TimeInForce
    fulfilled: float
    active: bool
