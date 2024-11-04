from src.factory.asset import Login
from src.factory.factory import AbstractFactory
__all__ = ['Factory']

# Factory instância classes concretas na qual referência classes Abstratas contendo tarefas solicitadas
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
        
        