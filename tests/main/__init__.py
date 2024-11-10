from collections import namedtuple
from src import *
__all__ = ['Schema']

class Schema:
    # Client Data-Class
    def __init__(self, Request: namedtuple = namedtuple("Request", ("username", "passwd", "path"))):
        self.__Request: tuple = Request
        self.__facade = iter(Facade(args=(x for x in (self.__Request))))
        next(self.__facade)
    
    def __iter__(self):
        queue = yield
        if 'QUEUE' in queue.upper():
            yield self.__facade.send(queue)
        else:
            send.close()
            exit(0)
        self.__facade.close()

