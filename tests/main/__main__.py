from __init__ import *
from template import *
__obj__ = (Schema, Template)
__all__ = [None]

if __name__ == '__main__':
    __main__ = None
    try:
        for obj in __obj__:
            if __main__ is not None:
                for line in obj(schema=__main__): ...
            else:
                __main__ = obj
    except TypeError:
        ...
