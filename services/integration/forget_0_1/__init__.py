from threading import Thread
from itertools import islice, starmap

from abs import SocketAbstract
from main import SenderLiveServer, SenderLiveClient



# FACTORYS (Fábricas)

class FactoryServer(SocketAbstract):

    def __init__(self):
        super().__init__('localhost', 8888)

    
    def __call__(self):
        xsocket = iter(self)
        sock, _ = starmap(tuple, [next(xsocket), next(xsocket)])
        threads = [Thread(target=SenderLiveServer(), args=(sock[0], self, sock[1],))]
        try:
            [thread.start() for thread in threads]
            print("-- ESCUTA EM ABERTO\nlocal:\t%s --" % (sock[1],))
            
            msg = input("\nServer Enter prompt: ")
            while True:
                self.put("Server:\t%s" % msg)

                msg = input("\nServer Enter prompt: ")
            [thread.join() for thread in threads]
        except KeyboardInterrupt:
            sock[0].close()
            exit()



class FactoryClient(SocketAbstract):
    def __init__(self):
        super().__init__('localhost', 8888)
    
    def __call__(self):
        xsocket = iter(self)
        sock, _ = starmap(tuple, [next(xsocket), next(xsocket)])
        threads = [Thread(target=SenderLiveClient(), args=(sock[0], self, sock[1],))]

        [thread.start() for thread in threads]
        msg = input("\nClient Enter prompt: ")
        while True:
            self.put(msg)
            msg = input("\nClient Enter prompt: ")

            [thread.join() for thread in threads]
        sock[0].close()
        exit()