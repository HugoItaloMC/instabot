#  GERENCIADORES DO CHROMEDRIVER
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.factory.factory import *
__all__ = ['Factory']

# Factory, classe concreta de AbstractFactory que acessa classes Concretas através de métodos
class Factory(AbstractFactory):
    def __init__(self, data: tuple, users):
        super().__init__()
        self.__data: tuple = data
        self.__users: set = users
    
    def __iter__(self):
        yield
        TASKS = (self._login(data=self.__data), 
                self._comment(users=self.__users), 
                self._like(users=self.__users), 
                self._follow(users=self.__users), 
                self._unfollow(users=self.__users))
        for task in TASKS:
            xbool: bool = yield task
        raise StopIteration
        

        