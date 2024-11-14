from __init__ import *
from template import *
__all__ = [None]

if __name__ == '__main__':
    try:
        __main__ = None
        for __obj__ in (Schema, Template) :
            if __main__ is not None:
                for line in __obj__(schema=__main__): ...
            else:
                __main__ = __obj__
    except TypeError:
        ...
