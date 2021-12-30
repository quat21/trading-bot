'''
Define an abstract Strategy class that defines the interface for a trading
strategy.
'''

from abc import ABC, abstractmethod
from helper import Status


class AbstractBot(ABC):
    '''Interface for any trading strategy.'''

    def __init__(self, exchange):
        '''Initialize trading strategy.'''
        self.exchange = exchange
        self.status = Status.STARTING
        self.stop = False

    @abstractmethod
    def start(self) -> None:
        '''Start the trading bot. Stop if false == True.'''

    @abstractmethod
    def get_description(self) -> str:
        '''Return a string that describes the trading strategy.'''
