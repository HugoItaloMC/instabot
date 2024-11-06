from typing import Generator, Coroutine
from queue import Queue

from src.factory import *
__all__ = ['Facade']

class Facade:
    # chama Wrapper passando qual factory utilizar

    def __init__(self, args: Generator):
        # args
        self.__queue = Queue()
        self.__args: Generator[Coroutine] = args
        self.__data: tuple = (next(self.__args), next(self.__args))
        self.__factory = iter(Factory(self.__data))
        self.__queue.put(self.__factory)
    
    def __iter__(self):
        send = yield
        if 'QUEUE' in send.upper():
            yield self.__queue

