from typing import Generator, Coroutine
from queue import Queue

from src.factory import Factory
__all__ = ['Facade']

class Facade:
    # chama Wrapper passando qual factory utilizar

    def __init__(self, args: Generator):
        # args
        self.__queue = Queue()
        self.__args: Generator[Coroutine] = args
        self.__data: tuple = (next(self.__args), next(self.__args))
        self.__factory = iter(Factory(self.__data))
        self.__queue.put(self.__factory)
    
    def __iter__(self):
        send = yield
        if 'QUEUE' in send.upper():
            yield self.__queue
        """
        ### Trazendo factory para chamada de pilha com a instância de `Wrapper` ###
        
        # Enviando tarefa com funcões auxiliares
        if self.__args:
            wrapper = iter(Wrapper(self.__op, self.__data, self.__args[0]))  
        
        # Enviando tarefas sem funcões auxiliares
        if wrapper is None:
            wrapper = iter(Wrapper(self.__op, self.__data))

        # Iniciando tareas
        # Iniciando a corroutina de `Wrapper`
        next(wrapper)  
        
        # Aqui comecamos a trabalhar com a Factory podendo administrar métodos e atributos que contém as regras para tarefas
        send = yield  
        if 'SET' in send.upper():
            recv = wrapper.send('INIT')  # Referênciando Factory em uma  `Queue` como um generator
            queue = next(recv)  # recolhendo `Queue` do generator
            factory = queue.get()  # buscando Factory contida na `Queue`
            #factory.attr = 'test'  # Adiministrando novos atributos para a factory
            #factory.impar()  # Tarefa de alto nível, ñ altera o estado e saída da classe concreta da Factory
            yield factory.flush()  # Enviando o estado e saída da Factory através de corroutina

        wrapper.close()
        yield from self
        """

    
    

