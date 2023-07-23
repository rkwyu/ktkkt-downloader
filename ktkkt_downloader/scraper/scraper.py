from abc import ABC, abstractmethod
from typing import Union

from ..object import Episode
from .strategy import Strategy

# context
class Scraper():
    def set_strategy(self, strategy:Strategy):
        self.strategy = strategy

    def get_series(self, url:str) -> list:
        return self.strategy.get_series(url)
    
    def get_episode(self, url:str) -> Episode:
        return self.strategy.get_episode(url)
    
    def get_m3u8(self, url:str) -> str:
        return self.strategy.get_m3u8(url)