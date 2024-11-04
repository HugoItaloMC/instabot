from src.factory.tools.utils import Login
from src.factory.abs import AbstractLike, AbstractComment, AbstractFollow, AbstractUnfollow

__all__ = ['Factory']


class Like(AbstractLike): flush = ...

class Comment(AbstractComment): flush = ...

class Follow(AbstractFollow): flush = ...

class Unfollow(AbstractUnfollow): flush = ...


# Factory, chama classes concretas na qual referência classes Abstratas contendo tarefas solicitadas pelo frontend
class Factory:
    def __init__(self, data: tuple):
        self.__data = data
    
    def __iter__(self):
        tasks = yield
        yield Login(self.__data)  # Default

        while tasks:
            if 'comment' in tasks:
                tasks.discard('comment')
                yield Comment()
            
            elif 'like' in tasks:
                tasks.discard('like')
                yield Like()
            
            elif 'follow' in tasks:
                tasks.discard('follow')
                yield Follow()
            
            elif 'unfollow' in tasks:
                tasks.discard('unfollow')
                yield Unfollow()
            else:
                tasks.close()
        yield
        
        