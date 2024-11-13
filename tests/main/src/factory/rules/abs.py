# GERENCIADOR DE ELEMENTOS DA PÁGINA WEB
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.factory.core import *
from src.utils.sleepnice import delay
__all__ = ['AbstractLike', 'AbstractComment', 'AbstractFollow', 'AbstractUnfollow', 'AbstractLogin']


class AbstractLogin(Handler):

    def __init__(self, data: tuple):
        super().__init__()
        self._data: tuple = data
    
    
    def __next__(self):
        +self
        if self._driver is not None:
            actions = ActionChains(self._driver)
        while self._exit > 0:
            -self
            try:
                self._driver.maximize_window()
                self._driver.get('https://www.instagram.com')
                delay('LOW')
                # PUT USERNAME
                self._driver.find_element(By.NAME, 'username').send_keys(self._data[0])
                    
                # PUT PASSWORD
                self._driver.find_element(By.NAME, 'password').send_keys(self._data[1])

                # BUTTON LOGIN
                self._driver.find_element(By.NAME, 'password').send_keys(u'\ue007')
                delay('LOW')

                # POP-UP BOT IDENTIFICADO
                try:
                    delay('LOW')
                    actions.move_to_element(WebDriverWait(self._driver, 10).until(
                    EC.elemento_to_be_clickable((By.XPATH, "//span[contains(text(), 'Ignore')]")))).click().perform()    
                    print("BOT IDENTIFICADO")
                except Exception as e:
                    print("BOT Ñ IDENTIFICADO")
                
                # Ñ SALVAR INFORMACÕES DE LOGIN
                try:
                    delay('LOW')
                    actions.move_to_element(WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not now')]")))).click().perform()
                except Exception as e:
                    print(e)
                
                try:
                    delay('LOW')
                    # Ñ PERMITIR NOTIFICACÕES
                    actions.move_to_element(WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now')]")))).click().perform()
                except Exception as e:
                    print('Ń pediu para enviar notificacões')

            # MAIN EXCEPTION 
            except Exception as e:
                print(e)
        else:
            +self
            ~self
            raise StopIteration

class AbstractLike(Handler):

    def __init__(self):
        super().__init__()
    
    def __next__(self):
        +self            
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            +self
            ~self
            raise StopIteration


class AbstractComment(Handler):


    def __init__(self):
        super().__init__()
    
    def __next__(self):
        +self            
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            +self
            ~self
            raise StopIteration


class AbstractFollow(Handler):


    def __init__(self):
        super().__init__()
    
    def __next__(self):
        +self
            
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            +self
            ~self
            raise StopIteration


class AbstractUnfollow(Handler):

    def __init__(self):
        super().__init__()

    def __next__(self):
        +self    
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            +self
            ~self
            raise StopIteration
