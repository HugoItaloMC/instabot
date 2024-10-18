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
    

    def __next__(self):
        if not self.__idx:
            print("INSERINDO USERNAME E PASSWORD:")
            delay()
            print("LOGIN CONCLUÍDUO\n...")

            self.__idx += 1

            # CHAMAR OBJETO COMO FUNCÃO/MÉTODO
            self()

            if self.__idx == 2:

                try:
                    # SE BOT Ñ FOI IDENTIFICADO VERIFICAR RECAPTCHA
                    print('VERIFICANDO RECAPTCHA')
                    solver = CaptchaSolver("teste_driver")
                    for step in solver:
                        pass
                    self.__idx += 1
                except Exception as err:
                    print("## ERROR ##:\t%s" % err)
                else:
                    print("RECAPTCHA VERIFICADO")
                    delay()
                finally:
                    print("SALVANDO INFORMACÕES DE LOGIN")
                    delay()
    
    
    def __call__(self):
        if self.__idx:
            print("VERIFICANDO SE BOT FOI IDENTIFICADO")
            bot_identificado: bool = None
            
            # BUSCANDO POP-UP DE BOT IDENTIFCADO
            try:
                op = random.choice([False, True])
                bot_identificado = op

                if bot_identificado:
                    print("BOT IDENTIFICADO")
                else:
                    print("BOT Ñ IDENTIFICADO")
                    self.__idx += 1

            except Exception as err:
                print('%s' % err)

if __name__ == '__main__':
    login = iter(InstaLogin('driver_teste', 'data_teste'))
    next(login)

