from src.factory.core import Handler


class AbstractLike(Handler):

    def __init__(self):
        super().__init__()
    
    def __next__(self):
        +self            
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            raise StopIteration
    """
    def __next__(self):
        if not self._exit and self.__arg:
            +self

            while self._exit > 0:
                -self
            
            if 'par' in self.__args:
                self.__args.discard('par')
                self.__arg = PairNumber(self.__arg)()

            xdata = self.__arg.pop()
            print(xdata)
        else:
            print("TAREFA `N` concluída")
            +self
            raise StopIteration
    """


class AbstractComment(Handler):


    def __init__(self):
        super().__init__()
    
    def __next__(self):
        +self
            
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            raise StopIteration
    """
    def __next__(self):
        if not self._exit and self.__arg:
            +self

            while self._exit > 0:
                -self
            
            if 'par' in self.__args:
                self.__args.discard('par')
                self.__arg = PairNumber(self.__arg)()

            xdata = self.__arg.pop()
            print(xdata)
        else:
            print("TAREFA `N` concluída")
            +self
            raise StopIteration
    """


class AbstractFollow(Handler):


    def __init__(self):
        super().__init__()
    
    def __next__(self):
        +self
            
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            raise StopIteration
    """
    def __next__(self):
        if not self._exit and self.__arg:
            +self

            while self._exit > 0:
                -self
            
            if 'par' in self.__args:
                self.__args.discard('par')
                self.__arg = PairNumber(self.__arg)()

            xdata = self.__arg.pop()
            print(xdata)
        else:
            print("TAREFA `N` concluída")
            +self
            raise StopIteration
    """


class AbstractUnfollow(Handler):


    def __init__(self):
        super().__init__()

    def __next__(self):
        +self    
        while self._exit > 0:
            -self
            print('Executando Next de %s' % self)
        else:
            raise StopIteration
    """
    def __next__(self):
        if not self._exit and self.__arg:
            +self

            while self._exit > 0:
                -self
            
            if 'par' in self.__args:
                self.__args.discard('par')
                self.__arg = PairNumber(self.__arg)()

            xdata = self.__arg.pop()
            print(xdata)
        else:
            print("TAREFA `N` concluída")
            +self
            raise StopIteration
    """
