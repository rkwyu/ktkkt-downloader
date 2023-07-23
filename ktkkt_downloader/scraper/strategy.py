from abc import ABC, abstractmethod

class Strategy():
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def get_series(self, url:str):
        return
    
    @abstractmethod
    def get_episode(self, url:str):
        return
    
    @abstractmethod
    def get_m3u8(self, url:str):
        return
    