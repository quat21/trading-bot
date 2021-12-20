'''
Define required classes for modelling an action that a trading strateg
could take.
'''

from enum import Enum, auto


class Move(Enum):
    '''Define possible actions that a trading strategy can decide on.'''
    PLACE_BUY_BORDER = auto()
    PLACE_SELL_ORDER = auto()
    CANCEL_ORDER = auto()
    WAIT = auto()


class TimeInForce(Enum):
    '''Define possible times in force for an order.'''
    GTC = auto()
    IOC = auto()
    FOK = auto()


class NewOrder:
    '''
    Contains all information for an action that a trading strategy can take.
    '''

    def __init__(self, move: Move, params: dict):
        self.move = move
        self.params = params


class CancelRequest:
    '''Contains all information for removing an order.'''
