# FACADE (Faixada de subsistemas)
import json
import random
from time import sleep


#  GERENCIADORES DO CHROMEDRIVER
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# GERENCIADOR DE ELEMENTOS DA PÁGINA WEB
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# PIPES PARA GERENCIAR O INSTAGRAM (LOGIN, CURTIR, COMENTAR, SEGUIR, DESEGUIR)
from pipes.pipe_like import PipeInstaLike
from pipes.pipe_login import PipeInstaLogin

# UTILS
from utils.cookies_manager import CookiesManager
from utils.sleepnice import delay

class Driver:
    # OBJETO QUE TEM A INSTÂNCIA PRINCIPAL DO WEBDRIVER

    def __init__(self, data: tuple, operation, *args):
        self.data = data
        self.operation: list = operation
        self.args = args

    def __iter__(self):
        self._options = webdriver.ChromeOptions()
        self._options.add_argument("--start-minimized")
        self._options.add_argument("--disable-extensions")  # Desabilita extensões defaults Chrome
        self._options.add_argument("--disable-popup-blocking")  # Desabilita bloqueio de popup's
        self._options.add_argument("--incognito")  # Abre em modo anônimo
        self._options.add_argument("--profile-directory=Default")  # Usar o perfil padrão
        self._options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')  # User agent do Chrome no Linux")
        self._options.add_argument("--disable-blink-features=AutomationControlled")  # Impede detectacão de automacão
        self._options.add_argument("--enable-features=BlockThirdPartyCookies")  # Bloqueia Cookies de Terceiros
        self._options.binary_location = '/usr/bin/google-chrome'  # Localizacão Chrome
        # Iniciando driver juntamente com protocolo de iteracão no objeto
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self._options)
        self.driver.maximize_window()  # MAXIMIZANDO TELA
        self.cookie_renew: bool = self.args[0]
        self.cookie_release: bool = self.args[1]
        self._idx = 0
        return self
    
    def __next__(self):
        if not self._idx:
            try:
                # OPEN DRIVER CHROME WITH WEB-SITE 
                self.driver.get("https://www.instagram.com")
                delay('low')

                # PUT USERNAME
                self.driver.find_element(By.NAME, 'username').send_keys(self.data.username)
                delay()
                # PUT PASSWORD
                self.driver.find_element(By.NAME, 'password').send_keys(self.data.passwd)
                delay()
                # BUTTON LOGIN
                self.driver.find_element(By.NAME, 'password').send_keys(u'\ue007')
                delay('nice')
                self()
                self._idx += 1
            except StopIteration:
                return self._idx
    
    def __call__(self, *args, **kw):
        actions = ActionChains(self.driver)

        try:
            # POP BOT IDENTIFICADO
            ignorar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Ignorar')]")))
            print("## WARNING ##: BOT IDENTIFICADO")
            actions.move_to_element(ignorar).click().perform()
        except Exception:
            print("## INFO ## : \t 'BOT NAO IDENTIFICADO'")

            # ARMAZENAR CONTA NA SESSÃO DO BROWSER
            agora_nao_armazenar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Salvar informações')]")))
            actions.move_to_element(agora_nao_armazenar).click().perform()

            # Ñ PERMITIR NOTIFICACÕES
            agora_nao_notificacoes = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Agora não']")))
            actions.move_to_element(agora_nao_notificacoes).click().perform()

            self.driver.refresh()
        delay()

        # Gerenciar Cookies ###############################
        if self.cookie_release:
            cookies = iter(CookiesManager(self.driver, 
                            self.data.username, 'release'))
            next(cookies)
        
        if self.cookie_renew:
            cookies = iter(CookiesManager(self.driver, 
                            self.data.username, 'renew'))
            next(cookies)
        ####################################################


        # CHAMANDO OPERACÃO DEFINIDA
        if self.operation == "LIKE":

            pipe_like = iter(PipeInstaLike(driver=self.driver, path=self.data.path))
            next(pipe_like)
