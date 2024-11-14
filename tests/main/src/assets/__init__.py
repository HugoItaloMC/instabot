from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
__all__ =['SeleniumDriver']


class DriverDescriptor:
    def __get__(self, instance, owner):
        if instance._driver is ...:
            options = webdriver.ChromeOptions()
            options.add_argument('user-data-dir=$HOME')
            options.add_argument("--start-minimized")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--incognito")
            options.add_argument("--profile-directory=Default")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--enable-features=BlockThirdPartyCookies")
            options.binary_location = '/usr/bin/google-chrome'
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)

            instance._driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            
            # Executa JavaScript para ocultar o WebDriver
            instance._driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            # Define User-Agent e Headers HTTP
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                        "(KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.5",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Referer": "https://www.instagram.com/"}
            
            instance._driver.execute_cdp_cmd('Network.setUserAgentOverride', 
                                             {'userAgent': headers["User-Agent"],
                                              "acceptLanguage": headers["Accept-Language"]})
            
            instance._driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', 
                                             {'headers': headers})
            
        return instance._driver

    def __set__(self, instance, value):
        instance._driver = value


class SeleniumDriver:
    _driver: 'selenium.webdriver' = ...  # Atributo controlado pelo descritor
    
    driver = DriverDescriptor()

    def __new__(cls, *arg, **kw):
        # Singleton webdriver
        if not hasattr(cls, '_instance'):
            cls._instance = super(SeleniumDriver, cls).__new__(cls, *arg, **kw)
        return cls._instance
