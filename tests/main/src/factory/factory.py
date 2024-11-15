from src.factory.rules import * 
__all__ = ['AbstractFactory']

# AbstractFactory instância classes Concretas que herdam de classes Abstratas contendo tarefas solicitadas
class AbstractFactory:
    # Refrênciando classes concretas em atributos  métodos

    def _login(self, data: tuple):
        return Login(data)

    def _like(self, users: set):
        return Like(users=users)

    def _comment(self, users: set):
        return Comment(users=users)
    
    def _follow(self, users: set):
        return Follow(users=users)
    
    def _unfollow(self, users: set):
        return Unfollow(users=users)
    
