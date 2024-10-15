import asyncio
import subprocess
from queue import Queue
from abc import ABCMeta, abstractmethod
from socket import (socket, AF_UNSPEC, SOCK_STREAM, AI_PASSIVE, SO_REUSEADDR, SOL_SOCKET, getaddrinfo, SocketType)


# OBJETOS ABSTRATOS

class SocketAbstract(metaclass=ABCMeta):
    # Super classe responsável pelo servidor socket que vai iniciar a conexão

    
    def __init__(self, *args):
        self.args = args
        
    def __iter__(self):  
        self.__msg = str()
        self.new = True
        self.con = None
        self._socket: SocketType
        self.__idx = 0
        return self
    

    def __next__(self):
        # BUSCA INFORMACÕES DO ENDERECO EM QUE VAI INICIAR O SOCKET
        

        if not self.__idx:
            try:
                for info_addr in getaddrinfo(self.args[0], self.args[1], AF_UNSPEC, SOCK_STREAM, 0, AI_PASSIVE):
                    AF_, SOCKET_TYPE, PROTOCOL, CANONNAME, ADDR = info_addr
                else:
                    self.__idx += 1
                    self._socket = socket(AF_, SOCKET_TYPE, PROTOCOL)
                    self._socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
                    yield (self._socket, ADDR)
            except StopIteration:
                return self.__idx
                
        
    def put(self, msg):
        self.__msg = msg
        if self.con is not None:
            self.con.send(str.encode(self.__msg))
        
        
    def get(self):
        return self.__msg

    
    def loop(self):
        return self.new


class SenderLiveAbstract(metaclass=ABCMeta):

    
    def __iter__(self, arg):
        self.arg = arg
        self.__output = subprocess.run(self.arg, stdin=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        self.__idx = 0
        return self
    
    def __next__(self):
        if not self.__idx:
            try:
                print(self.__output.stderr)
            except StopIteration:
                return self.__idx


if __name__ == '__main__':
    """  
    
    [OK] ## TESTS `SocketServerAbstract`
    xsocket = iter(SocketServerAbstract('localhost', 8888))
    sock_infos = "".join(map(str, next(xsocket)))
    addr_infos = "".join(map(str, next(xsocket)))
    print(sock_infos, addr_infos, xsocket.__dict__)
    
    
    [OK] ## TESTS `SenderLiveAbstract`
    sender_live = iter(SenderLiveAbstract("python3 services/app/run.py --username 'italo.corrreia' --passwd 'Acesso93#&' --path '/home/italo/Documentos/more/work_flow/services/instabot/db/data.json' --op 'LIKE' --login"))
    next(sender_live)
    """
    

                