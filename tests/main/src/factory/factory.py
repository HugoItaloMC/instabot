from src.factory.abstracts import * 
__all__ = ['AbstractFactory']
#### CONCRETS CLASS  ########################
#`run` refrência descritor da classe Handler#
class Like(AbstractLike): run = ...         #
                                            #
class Comment(AbstractComment): run = ...   #
                                            #
class Follow(AbstractFollow): run = ...     #
                                            #
class Unfollow(AbstractUnfollow): run = ... #
#############################################

# AbstractFactory instância classes Concretas que herdam de classes Abstratas contendo tarefas solicitadas
class AbstractFactory:
    # Refrênciando classes concretas em atributos  métodos

    def _like(self):
        return Like()

    def _comment(self):
        return Comment()
    
    def _follow(self):
        return Follow()
    
    def _unfollow(self):
        return Unfollow()
    
