import random, time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from recaptcha_solver import CaptchaSolver

### TOOL TO DELAY #######################################
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


class InstaLogin:


    def __init__(self, driver, data: tuple):
        self.driver = driver
        self.data = data
    
    def __iter__(self):
        self.__idx = 0
        return self
    

    def __next__(self) -> int:
        if not self.__idx:
            print("INSERINDO USERNAME E PASSWORD:")
            delay()
            print("LOGIN CONCLUÍDUO\n\n...\n")

            self.__idx += 1
            # CHAMAR OBJETO COMO FUNCÃO/MÉTODO
            self()   
            print("\nSALVANDO INFORMACÕES DE LOGIN")
            delay()
            self.__idx -= 1

            return self.__idx

    
    def __call__(self) -> None:
        if self.__idx:
            print("VERIFICANDO SE BOT FOI IDENTIFICADO")
            bot_identificado: bool = None
            verificar_recaptcha: bool = None
            
            # BUSCANDO POP-UP DE BOT IDENTIFCADO
            try:
                bot_identificado = False #random.choice([False, True])
                verificar_recaptcha = True #random.choice([False, True])

                if bot_identificado:
                    print("BOT IDENTIFICADO")
                    delay()
                    pass
                else:
                    delay()
                    print("Ñ DISPAROU POP-UP DE BOT IDENTIFICAO\n\nVERIFICAR SE SOLICITOU RECAPTCHA")   
                

                # VERIFICANDO SE TODAS ETAPAS DE `CaptchaSolver` foram concluídas.
                while verificar_recaptcha and (solver := CaptchaSolver('test_driver')()) and (1 << solver) % 2 == 0:
                    self.__idx += solver
                    break

            except Exception as err:
                print('%s' % err)


if __name__ == '__main__':
    print(next(iter(InstaLogin('driver_teste', 'data_teste'))))


