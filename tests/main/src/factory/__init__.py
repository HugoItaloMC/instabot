from src.factory.asset import Login
from src.factory.factory import *
__all__ = ['Factory']

# Factory, classe concreta de AbstractFactory que acessa classes Concretas através de métodos
class Factory(AbstractFactory):
    def __init__(self, data: tuple):
        super().__init__()
        self.__data = data
    
    def __iter__(self):
        tasks = yield
        yield Login(self.__data)  # Default

        while tasks:
            if 'comment' in tasks:
                tasks.discard('comment')
                yield self._comment()
            
            elif 'like' in tasks:
                tasks.discard('like')
                yield self._like()
            
            elif 'follow' in tasks:
                tasks.discard('follow')
                yield self._follow()
            
            elif 'unfollow' in tasks:
                tasks.discard('unfollow')
                yield self._unfollow()
                
            else:
                tasks.close()
        yield
        
        