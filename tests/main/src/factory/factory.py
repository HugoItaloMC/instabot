from src.factory.rules import * 
__all__ = ['AbstractFactory']

# AbstractFactory instância classes Concretas que herdam de classes Abstratas contendo tarefas solicitadas
class AbstractFactory:
    # Refrênciando classes concretas em atributos  métodos

    def _login(self, data):
        return Login(data)

    def _like(self):
        return Like()

    def _comment(self):
        return Comment()
    
    def _follow(self):
        return Follow()
    
    def _unfollow(self):
        return Unfollow()
    
