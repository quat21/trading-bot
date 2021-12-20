'''
Define an abstract Strategy class that defines the interface for a trading
strategy.
'''

from abc import ABC, abstractmethod
from action import NewOrder


class Strategy(ABC):
    '''Interface for any trading strategy.'''

    def __init__(self, data_handler):
        '''Initialize trading strategy.'''
        self.data_handler = data_handler
        super.__init__()

    @abstractmethod
    def decide_action(self) -> NewOrder:
        '''
        Decide on an action for the bot to take.
        '''

    @abstractmethod
    def stop(self) -> bool:
        '''
        Run cleanup processes an return true if everything went well.
        '''
