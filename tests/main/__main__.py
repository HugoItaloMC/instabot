from __init__ import *
from template import *
obj = (Schema, Template)
__all__ = [None]

if __name__ == '__main__':
    main = None
    for xobj in obj:
        if main is not None:
            for line in xobj(schema=main): ...
        else:
            main = xobj
