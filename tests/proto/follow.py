import json

### TOOL TO DELAY #######################################
import random
import time
def delay(frequency: str = ''):                         #
    frequency.lower()                                   #
    # frequency : ['low', 'nice', 'high']               #
    if frequency:                                       #
        timein: int = 0                                 #
        if frequency == 'low':                          #
            timein = time.sleep(random.randint(6, 11))  #
        elif frequency == 'nice':                       #
            timein = time.sleep(random.randint(9, 14))  #
        elif frequency == 'high':                       #
            timein = time.sleep(random.randint(12, 17)) #
        else:                                           #
            timein = time.sleep(random.randint(2, 4))   #
        return timein                                   #
#########################################################


class InstaFollow:

    def __init__(self, driver, path):
        self.driver = driver
        self.path = path
    

    def __iter__(self):
        self.__state = False  # Se tarefas forem concluídas alterna o estado
        self.__idx = 0  # Controla pilha de tarefas
        

        print("\nINICIANDO TAREFA (SEGUIR)")
        delay()
        print("USUÁRIOS CARREGADOS")

        # CARREGANDO USUÁRIOS EM ARQUIVO EXTERNO
        with open(self.path, "r+") as file:
            self.__users = set(json.loads(file.read())['users'])
        delay()
        print("USUARIOS=%s" % self.__users)

        return self

    # administrar estado e indice utilizando operadores unários
    def __pos__(self):

        # operador unário +obj
        # administrar número positivos
        # EX: c = Class(25) ; print(+c) # 25
        if not self.__idx:
            self.__idx += 1
            self
            return  self.__idx
        
    def __neg__(self):
        # operador unário -obj
        # administrar números negativos
        #   # EX: c = Class(25) ; print(-c) # -25
        self.__idx -= 1
        return self.__idx


    # Administrar estado
    def __invert__(self):
        # operador unário ~obj
        # inverto o estado bit a bit do objeto
        # EX: c = Class() ; print(~c) # True ; print(~c) # False
        self.__state = not self.__state
        return self.__state


    def __next__(self):
        if not self.__idx and self.__users:
            global user
            
            +self
            while self.__idx > 0:
                -self
                user = self.__users.pop()
                print("\n\nABRINDO PÁGINA DO USUÁRIO\nUSER=%s" % user)
                delay()
                
                print("SEGUINDO USUÁRIO\n%s" % user)
                delay()
        else:
            print("TODAS USUÁRIOS SEGUIDOS, ÚLTIMO USUÁRIO (%s)" % user)
            +self
            raise StopIteration
    
    def __call__(self):
        iter(self)
        while True:
            try:
                next(self)
            except StopIteration:
                ~self
                return self.__idx, self.__state,

if __name__ == '__main__':
    while (follow := InstaFollow('test_driver', 'data.json')()) and (1 << follow[0]) % 2 == 0:
        print(follow)
        break