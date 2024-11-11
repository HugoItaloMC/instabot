from typing import Generator, Coroutine

from src.factory import *
__all__ = ['Facade']

class Facade:
    # chama Wrapper passando qual factory utilizar

    def __init__(self, args: Generator):
        # args
        self.__args: Generator[Coroutine] = args
        self.__data: tuple = (next(self.__args), next(self.__args))
        self.__factory: object = iter(Factory(self.__data))
    
    def __iter__(self):
        send: str = yield self.__factory
        raise StopIteration

