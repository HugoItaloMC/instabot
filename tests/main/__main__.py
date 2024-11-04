from collections import namedtuple

from src import Facade
from template import Template

class Schema:
    # Client Class
    def __init__(self, Request: namedtuple = namedtuple("Request", ("username", "passwd", "path"))):
        self.__Request: tuple = Request
        self.__facade = iter(Facade(args=(x for x in (self.__Request))))
        next(self.__facade)
    
    def __iter__(self):
        send = yield
        if 'DISPATCH' in send.upper():
            yield self.__facade.send('QUEUE')
        else:
            send.close()
            exit(0)
        facade.close()

if __name__ == '__main__':
    for template in Template(schema=Schema): ...
    