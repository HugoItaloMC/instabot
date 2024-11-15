from typing import Generator, Coroutine

from src.factory import *
from src.utils import *
__all__ = ['Facade']

class Facade:
    #  Chama factory

    def __init__(self, args: Generator):
        self.__args: Generator[Coroutine] = args  # GENERATOR EXPRESSION
        data: tuple = (next(self.__args), next(self.__args))
        users: set = iter(UsersJsonUtils(path=next(self.__args)))  # GENERATOR
        self.__factory: object = iter(Factory(data=data, users=next(users)))
    
    def __iter__(self):
        yield self.__factory
        raise StopIteration

