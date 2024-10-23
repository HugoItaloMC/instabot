from collections import namedtuple

from login import InstaLogin
from like import InstaLike
from comment import InstaComment


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




class Driver:


    # CONSTRUTOR DO OBJETO
    def __init__(self, data: namedtuple, operations: tuple, *args):
        self.data = data
        self.operations: tuple = operations
        self.args = args
    

    # ACIONANDO ATTRS DE CLASSE APÓS A CHAMADA DE `iter()`
    def __iter__(self):
        print("INICIANDO DRIVER")
        self.__steps = set(self.operations)  # ESTRUTURA `CONJUNTO (set)` Ñ PERMITE REPETICÃO DE DADOS

        ## DEFAULT PIPES ##########################
        self.__pipes: dict = dict(LIKE=InstaLike, ########################################                                                                                 
                                COMMENT=InstaComment, FOLLOW='PIPE PRA SEGUIR USUÁRIO', ##
                                UNFOLLOW='PIPE PARA DEIXAR DE SEGUIR USUÁRIO')          ##
        ##################################################################################
        
        self.__driver = 'THE WEBDRIVER SELENIUM'
        self.__idx = 0
        
        return self  # RETORNANDO OBJETO COMO PROTOCOLO DO ITERADOR
        
    
    def __next__(self):

        print("VERIFICADO TAREFAS (login, like, follow, unfollow, comment, etc)")
            
        ## DEFAULT COROUTINA ##############################################
        ##  A instância InstaLogin deve ser concluída por default esta   ##
        ## consiste em etapas essensiais para a conclusão das tarefas    ##
        ## como, analisar se o bot foi identificado, concluir ReCaptCha, ##
        ## eventos em pop-ups após o login.                              ######################################################
        if not self.__idx and self.__steps and (1 << next(iter(InstaLogin(driver=self.__driver, data=self.data)))) % 2 == 0: ##
            self.__idx += 1                                           
            
            global op
            ## APÓS O LOGIN, CONCLUIR ETAPAS RECEBIDAS ATRAVÉS DA NAMESPACES ##
            while self.__idx > 0:                        
                self.__idx -= 1                          
                try:                                     
                    # EXECUTANDO TAREFAS                 
                    while (op := self.__pipes[self.__steps.pop()](self.__driver, 'data.json')()) < 2: 
                        self.__idx += op
                        break
                    
                except KeyError:
                    return self.__idx
                except Exception as err:
                    print("## ERR ##:\t%s" % err)
                                          
        else:  ## TODAS TAREFAS CONCLUÍDAS ###
            raise StopIteration


    def __call__(self):
        #  Internamente o loop `for` faz chamadas com método next()
        # até `StopIteration` set True, somente objetos seguindo
        # protocolo do iterador podem ser iterados.
        iter(self)
        while True:
            try:
                next(self)
            except StopIteration:
                return self.__idx
            except Exception as err:
                self.__idx += 1
                print("## ERROR ##:\t%s" % err)
                return self.__idx

if __name__ == '__main__':

    # A classe Driver retorna 0, se retornar qualquer valor alguma excessão foi levantada
    while not (driver := Driver('test_data', ('LIKE','COMMENT'))()) and not driver:
        print('OK')
        break
    else:
        print('FAILED')
    