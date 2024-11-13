#  GERENCIADORES DO CHROMEDRIVER
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.factory.factory import *
__all__ = ['Factory']

# Factory, classe concreta de AbstractFactory que acessa classes Concretas através de métodos
class Factory(AbstractFactory):
    def __init__(self, data: tuple):
        super().__init__()
        self.__data = data
    
    def __iter__(self):
        yield
        TASKS = (self._login(self.__data), 
                self._comment(), 
                self._like(), 
                self._follow(), 
                self._unfollow())
        for task in TASKS:
            xbool: bool = yield task
        

        