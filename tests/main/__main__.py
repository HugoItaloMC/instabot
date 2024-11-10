from __init__ import *
from template import *
__obj__ = (Schema, Template)
__all__ = [None]

if __name__ == '__main__':
    __main = None
    for obj in __obj__:
        if __main is not None:
            for line in obj(schema=__main): ...
        else:
            __main = obj
