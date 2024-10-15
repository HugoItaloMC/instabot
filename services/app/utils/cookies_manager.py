import json


class CookiesManager:

    def __init__(self, driver, *args):
        self.args = args
        self._driver = driver

    
    def __iter__(self):
        self.cookies = self._driver.get_cookies()

        # STORAGE COOKIES
        with open("cookies.json", "w+") as file:
            json.dump(self.cookies, file)
        
        self._driver.delete_all_cookies()
        self._driver.execute_script("localStorage.clear();")
        self._driver.execute_script("sessionStorage.clear();")
        self.__idx = 0
        return self
    
    def __next__(self):
        while not self.__idx:
            try:
                for cookie in self.cookies:
                    if 'expiry' in cookie:
                        del cookie['expiry']
                    self._driver.add_cookie(cookie)
                self._driver.refresh()
                self.__idx += 1
            except StopIteration:
                return self.__idx
