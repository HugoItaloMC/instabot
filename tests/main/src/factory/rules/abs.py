# DEFAULT PYTHON IMPORTS
import random

# GERENCIADOR DE ELEMENTOS DA PÁGINA WEB | PIP IMPORTS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# MY IMPORTS
from src.factory.core import *
from src.utils import delay
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
                    EC.elemento_to_be_clickable((By.XPATH, "//span[contains(text(), 'Dismiss')]")))).click().perform()    
                    print("BOT IDENTIFICADO")
                except Exception as e:
                    print("BOT Ñ IDENTIFICADO")
                
                # Ñ SALVAR INFORMACÕES DE LOGIN
                try:
                    delay('LOW')
                    actions.move_to_element(WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and @tabindex='0' and contains(text(), 'Not now')]")))).click().perform()
                except Exception as e:
                    print(e)

                
                # Ñ PERMITIR NOTIFICACÕES
                try:
                    delay('LOW')
                    actions.move_to_element(WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not')]")))).click().perform()
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

    def __init__(self, users: set):
        super().__init__()

        self.__users: set = users
    
    def __next__(self):
        +self
        actions = ActionChains(self._driver)            
        while (users := self.__users.copy()) and self._exit > 0:
            if self._driver is not None:
                -self
            while users:
                self._driver.get('http://www.instagram.com/%s' % users.pop())
                delay('HIGH')
                # SCROLL DOWN
                self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  
                delay('NICE')
                self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
                delay('LOW')

                # BUSCANDO PUBLICACÃO
                try:
                    self._driver.get("http://www.instagram.com/%s" % 
                        random.choice([link['href'] for link in BeautifulSoup(self._driver.page_source, 'html.parser').select('a', href=True) if '/p/' in link['href']]))
                    delay('LOW')

                    # CURTIR PUBLICACÃO        
                    actions.move_to_element(WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Like"')))).click().perform()
                    delay('LOW')

                except IndexError as e:
                    print("NENHUMA PUBLICACÃO ENCONTRADA")
                
                except Exception as e:
                    print(type(e))
                
            del users
            self._driver.get("http://www.instagram.com/")

        else:
            +self
            ~self
            raise StopIteration


class AbstractComment(Handler):


    def __init__(self, users: set):
        super().__init__()
        self.__users: set = users
    
    def __next__(self):
        +self            
        while (users := self.__users.copy()) and self._exit > 0:
            if self._driver is not None:
                -self
            while users:
                self._driver.get("https://www.instagram.com/%s" % users.pop())
                delay('LOW')
            else:
                if not users:
                    del users
                    break

        else:
            +self
            ~self
            raise StopIteration


class AbstractFollow(Handler):


    def __init__(self, users: set):
        super().__init__()
        self.__users: set = users
    
    def __next__(self):
        +self
            
        while (users := self.__users.copy()) and self._exit > 0:
            if self._driver is not None:
                -self
            actions = ActionChains(self._driver)
            while users:
                self._driver.get("https://www.instagram.com/%s" % users.pop())
                delay('LOW')

                # SEGUIR USUÁRIO
                try:
                    actions.move_to_element(WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@dir="auto" and contains(text(), "Follow")]')))).click().perform()
                    delay('LOW')
                except Exception as e:
                    print(type(e))
            
        else:
            +self
            ~self
            raise StopIteration


class AbstractUnfollow(Handler):

    def __init__(self, users: set):
        super().__init__()
        self.__users: set = users

    def __next__(self):
        +self    
        while (users := self.__users.copy())and self._exit > 0:
            if self._driver is not None:
                -self
            while users:
                self._driver.get("http://www.instagram.com/%s" % users.pop())
                delay('LOW')
        else:
            +self
            ~self
            raise StopIteration
