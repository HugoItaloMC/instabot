from src.factory.core import Handler
__all__ = ['AbstractLike', 'AbstractComment', 'AbstractFollow', 'AbstractUnfollow']

class AbstractLike(Handler):

    def __init__(self):
        super().__init__()
    
    def __next__(self):
        +self            
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            +self
            ~self
            raise StopIteration


class AbstractComment(Handler):


    def __init__(self):
        super().__init__()
    
    def __next__(self):
        +self            
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            +self
            ~self
            raise StopIteration


class AbstractFollow(Handler):


    def __init__(self):
        super().__init__()
    
    def __next__(self):
        +self
            
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            +self
            ~self
            raise StopIteration


class AbstractUnfollow(Handler):

    def __init__(self):
        super().__init__()

    def __next__(self):
        +self    
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            +self
            ~self
            raise StopIteration
