__all__ = [None]
if __name__ == '__main__':
    from __init__ import *
    from template import *
    
    try:
        #iter(Template(schema=Schema))
        __main__: Schema = None
        for __obj__ in (Schema, Template) :
            if __main__ is not None:
                for line in __obj__(schema=__main__): ...  # Template
            else:
                __main__ = __obj__  # Schema
    except TypeError:
        ...
