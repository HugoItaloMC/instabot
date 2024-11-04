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


class InstaComment:

    def __init__(self, driver, path):
        self.driver = driver
        self.path = path
    

    def __iter__(self):
        self.__idx = 0
        print("\nINICIANDO TAREFA (COMMENT)")
        delay()
        print("USUÁRIOS CARREGADOS")

        # CARREGANDO USUÁRIOS EM ARQUIVO EXTERNO
        with open(self.path, "r+") as file:
            self.__users = set(json.loads(file.read())['users'])
        delay()
        print("USUARIOS=%s" % self.__users)

        return self
    
    def __next__(self):
        if not self.__idx and self.__users:
            global user
            
            self.__idx += 1
            while self.__idx > 0:
                self.__idx -= 1
                user = self.__users.pop()
                print("\n\nABRINDO PÁGINA DO USUÁRIO\nUSER=%s" % user)
                delay()
                
                print("ABRINDO UMA PUBLICACÃO ALEATÓRIA")
                delay()

                print("VERIFICAR SE É POSSÍVEL COMENTAR NA PUBLICACÃO")
                if random.choice([False, True]):
                    delay()
                    print("COMENTÁRIPOS PERMITIDOS\nCOMENTANDO PUBLICACÃO")
                else:
                    print("PUBLICACÃO NÃO PERMITE COMENTÁRIOS")
                    
        else:
            print("TODAS PULICACÃO COMENTADAS, ÚLTIMO USUÁRIO (%s)" % user)
            self.__idx += 1
            raise StopIteration
    
    def __call__(self):
        iter(self)
        while True:
            try:
                next(self)
            except StopIteration:
                return self.__idx

if __name__ == '__main__':
    while (comment := InstaComment('test_driver', 'data.json')()) and (1 << comment) % 2 == 0:
        print(comment)
        break
