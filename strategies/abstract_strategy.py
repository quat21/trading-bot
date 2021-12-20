'''
Define an abstract Strategy class that defines the interface for a trading
strategy.
'''

from abc import ABC, abstractmethod
import enum


class Action(enum.Enum):
    '''Define possible actions that a trading strategy can decide on.'''
    BUY: 'test'
    SELL: 'test'
    NONE: 'potato'


class Strategy(ABC):
    '''Interface for any trading strategy.'''

    def __init__(self, data_handler):
        '''Initialize trading strategy.'''
        self.data_handler = data_handler
        super.__init__()

    @abstractmethod
    def decide_action(self) ->:
        '''
        Decide on an action for the bot to take.

        '''
