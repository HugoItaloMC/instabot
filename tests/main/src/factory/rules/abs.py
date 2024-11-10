from src.factory.core import Handler
__all__ = ['AbstractLike', 'AbstractComment', 'AbstractFollow', 'AbstractUnfollow', 'AbstractLogin']


class AbstractLogin(Handler):

    def __init__(self, data: tuple):
        super().__init__()
        self.data: tuple = data
    
    def __next__(self):
        +self
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            +self
            ~self
            raise StopIteration


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
