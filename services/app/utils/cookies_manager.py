import json
import asyncio
import aiofiles


from utils.sleepnice import delay


class CookiesManager:

    def __init__(self, driver, *args):
        self.args = args
        self._driver = driver

    
    def __iter__(self):
        print("## INFO ##:\tGERENCIANDO COOKIES")
        self._user = self.args[0]
        self._op = self.args[1]

        
        self.__idx = 0
        return self
    
    def __next__(self):
        while not self.__idx:            
            try:
                if self._op == 'renew':
                    print("## INFO ##:\t ARMAZENANDO COOKIES")
                    # ARMAZENAR COOKIES DE SESSÕES CONCLUÍDAS
                    self.cookies = self._driver.get_cookies()
                    with open("services/app/cookies@%s.json" % self._user, "w") as file:   
                        json.dump(self.cookies, file)       
                    

                #CASO QUEIRA UTILIZAR COOKIES DE SESSÕES ANTERIORES
                elif self._op == 'release':
                    self.__run(self)
                    delay()
                
                if self.__idx > 0:
                    self._driver.add_cookie(self.cookies)
                    self.__idx -= 1
                    
                self.__idx += 1

            except StopIteration:
                return self.__idx

            except Exception as err:
                print("## Error Manager cookies ##: %s" % err) 
    
    async def __call__(self):
        print("## INFO ##:\tUTILIZANDO COOKIES JÁ ARMAZENADOS")
        # ESVAZIAR STORAGE        
        #self._driver.execute_script("localStorage.clear();")
        #self._driver.execute_script("sessionStorage.clear();")

        # ESVAZIAR COOKIES
        self._driver.delete_all_cookies()
        
        # BUSCAR COOKIES JÁ ARMAZENADOS
        async with aiofiles.open("services/app/cookies@%s.json" % self._user, "r+") as file:
            cookies = json.loads(await file.read())
            
            for cookie in cookies:
                self.cookies = cookie
        self.__idx += 1
    
    def __run(self, method):
        # BUSCANDO EVENTO NA INSTÂNCIA
        make = asyncio.get_event_loop()

        # GERANDO TAREFA(s)
        task = make.create_task(method())

        # EXECUTANDO TAREFA
        make.run_until_complete(task)

        # AGRUPANDO TAREFAS
        tasks = asyncio.all_tasks(loop=make)
        gather = asyncio.gather(*tasks, return_exceptions=True)

        # EXECUTANDO TAREFAS AGRUPADAS
        make.run_until_complete(gather)

            
if __name__ == '__main__':

    teste = CookiesManager('teste `__call__`')
    teste()