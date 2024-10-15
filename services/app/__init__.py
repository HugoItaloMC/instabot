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

# PIPES PARA GERENCIAR O INSTAGRAM (CURTIR, COMENTAR, SEGUIR, DESEGUIR)
from pipes.pipe_like import PipeInstaLike

# UTILS
from utils.sleepnice import delay

class InstaDriver:
    # Objeto que realiza login no instagram

    def __init__(self, data: tuple, operation: str):
        self.data = data
        self.operation = operation

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
        self._idx = 0
        return self
    
    def __next__(self):
        if not self._idx:
            self._idx += 1
            # INIT LOGIN
            try:
                # OPEN DRIVER CHROME WITH WEB-SITE 
                self.driver.get("https://www.instagram.com")
                delay('low')

                # PUT USERNAME
                self.driver.find_element(By.NAME, 'username').send_keys(self.data.username)
                delay()

                # PUT PASSWORD
                self.driver.find_element(By.NAME, 'password').send_keys(self.data.passwd)
                delay('low')

                # BUTTON LOGIN
                self.driver.find_element(By.NAME, 'password').send_keys(u'\ue007')
                delay('nice')
                self()
            except StopIteration:
                return self._idx
    
    def __call__(self, *args, **kw):

        try:
            ignorar = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Ignorar')]")
            if ignorar.is_displayed():
                print("BOT IDENTIFICADO")
                ignorar.click()
            else:
                print("NENHUM ERRO AO LOGAR A CONTA")
        except Exception:
            print("## ERROR ## : \t 'BOT NAO IDENTIFICADO'")
        
        # Aguardando carregamento completo
        delay('high')
        # CHAMANDO OPERACÃO DEFINIDA

        if self.operation == "LIKE":
            pipe_like = iter(PipeInstaLike(driver=self.driver, path=self.data.path))
            next(pipe_like)
