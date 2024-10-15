# SUB-SISTEMA

import json
import random
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

from utils.cookies_manager import CookiesManager
from utils.sleepnice import delay

class PipeInstaLike:
    
    def __init__(self, driver, path):
        self.driver = driver
        self.path = path
    
    def __iter__(self):

        # Gerenciar Cookies #########################
        cookies = iter(CookiesManager(self.driver))
        next(cookies)
        ############################################

        delay('nice')
        self.__io = open(self.path, "r+")
        self.__idx = 0
        return self
    
    def __next__(self):
        if not self.__idx:

            try:
                xdata = json.loads(self.__io.read())
                users = set(xdata["users"])
                
                while users:
                    # AQUI QUERO ITERAR SOBRE O CONJUNTO IR ATÉ A PÁGINA DO ISNTAGRAM UTILIZANDO O DRIVER
                    # BUSCAR FOTOS ALEATÓRIAS E CURTIR DE FORMA RANDOMICA
                    user = users.pop()

                    delay('nice')
                    self.driver.get('https://www.instagram.com/%s' % user)
                    delay('low')
                    
                    # BUSCANDO FOTOS PARA CURTIR
                    soup = BeautifulSoup(self.driver.page_source , 'html.parser')
                    links_photo = soup.select("a", href=True)
                    
                    # FILTRAR LINKS DE FOTOS
                    href_links = [link['href'] for link in links_photo if '/p/' in link['href']]  
                    
                    # SELECIONAR LINK ALEATORIAMENTE
                    random_like = random.choice(href_links)
                    print('USER=(%s/%s)' % (user, random_like))
                    # BUSCANDO LINK PARA ABRIR FOTO
                    self.driver.get("https://www.instagram.com/%s" % random_like)
                    delay('nice')
                    actions = ActionChains(self.driver)
                    
                    ### CURTIR PHOTO ######################################################################
                    try:
                        photo = self.driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Curtir"]') or self.driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Descurtir"]')
                        delay('low')
                    except Exception as err:
                        self.driver.refresh()
                        delay('low')
                    else:
                        actions.move_to_element(photo).click().perform()
                        delay('nice')
                    finally:
                        self.driver.refresh()
                
                self.__idx += 1
                self.__io.close()
                raise StopIteration

            except KeyError:
                raise StopIteration
        