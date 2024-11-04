


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


class CookiesManager:

    def __init__(self, driver: 'webdriver', *args: tuple):
        self.__driver: 'webdriver' = driver  # WEB-DRIBER SELENIUM
        self.__args: tuple = args  # RECEBE PARAMETROS DE GERENCIAMENTO DE COOKIES (Usuário, Tarefa)

    
    def __iter__(self):
        self.__user: str = self.__args[0]
        self.__op: set = set(self.__args[1]) if not self.__args[1] == str else self.__args[1].split() # args[1]: tuple
        self.__idx: int = 0
        return self  # RETORNANDO ITERADOR DO OBJETO
    

    def __next__(self):
        if not self.__idx:
            while (idx := self()) and idx is not len(self.__op):
                raise StopIteration
            # NO TOTAL SÃO 2 OPERACÕES, CASO AS DUAS SEJA REALIZADAS FORMATAR INDICE PARA SEMPRE RETORNAR 1
        return (self.__idx - len(self.__args[1])) + 1 if len(set(self.__args[1])) == 2 else 0
    
    def __call__(self):
        try:
            while self.__op:

                op = self.__op.pop()

                if op == 'RELEASE':
                    print("UTILIZAR COOKIES JÁ ARMAZENADOS...")
                    delay()
                    self.__idx += 1
                elif op == 'RENEW':
                    print("ARMAZENAR COOKIES DE SESSÃO ATUAL...")
                    delay()
                    self.__idx += 1
                else:
                    print("OPERACÃO Ñ PERMITIDA")
                    delay()
                    self.__idx -= 1
                    break

        except StopIteration:
            return self.__idx
        
        except Exception as err:
            print("## ERR ##:\t%s" % err)
        

if __name__ == '__main__':
    cookiesmgr =  iter(CookiesManager('test_driver', 'oitalocorreia', ('RELEASE', 'RENEW')))
    next(cookiesmgr)