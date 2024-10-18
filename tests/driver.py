from collections import namedtuple

#from login import PipeInstaLogin

class Driver:

    def __init__(self, data: namedtuple, operations: list, *args):
        self.data = data
        self.operations: list = operations
        self.args = args
    
    def __iter__(self):
        self.__steps = set(self.operations)
        self.__driver = 'THE WEBDRIVER SELENIUM'
        self.__idx = 0
        return self
        
    
    def __next__(self):
        if self.__idx >= len(self.operations):
            raise StopIteration

        elif self.__idx == 0:
            #login = PipeInstaLogin(driver=self.__driver, data=self.data)
            #for xlogin in login:
             #   pass
            self.__idx += 1
            return
        
        elif self.__idx == 1:
            while self >= len(self.__steps):
                step = self.__steps[self.__idx]
                self(step)
                self.__idx += 1

    def __call__(self):
        return self.__mainloop()
    
    def __mainloop(self):
        for step in self:
            pass

    
    
    

if __name__ == '__main__':
    Data = namedtuple('Data', ("name", "passwd"))
    data = Data(name="italo.corrreia", passwd="SenhaTeste")
    driver = iter(Driver(data=data, operations=["LIKE", "FOLLOW", "COMMENT"]))
    next(driver)
    driver.send(True)
    
    