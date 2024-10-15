from threading import Thread, RLock
from abs import SenderLiveAbstract


# OBJETOS CONCRETOS

class SenderLiveServer(SenderLiveAbstract):

    def __init__(self):
        self._lock = RLock()
    
    def __iter__(self):
        return super().__iter__()
    
    def __call__(self, *args):
        self.args = args
        _socket = self.args[0]
        object_send = self.args[1]
        target_port = self.args[2]
        print(self.args)
        _socket.bind(target_port)
        _socket.listen(5)

        while True:
            client_socket, addr = _socket.accept()
            print("[*] -- CLIENTE CONECTADO\nlocal:\t%s --" % (addr,))
            threads = [Thread(target=object_send.con, args=(client_socket,))]
            [thread.start() for thread in threads]

            while True:
                with self._lock:
                    prompt = client_socket.recv(1024)
                    iter(self(prompt))
                    next(self)      
                [thread.join() for thread in threads]


class SenderLiveClient(SenderLiveAbstract):
    
    def __init__(self):
        self._lock = RLock()
        super().__init__()
    
    def __iter__(self):
        return super().__iter__()
    
    def __call__(self, *args):
        self.args = args
        _socket = self.args[0]
        object_send = self.args[1]
        target_port = self.args[2]
        print(self.args)
        _socket.connect(target_port)
        while object_send.loop():
            print("-- INICIANDO CLIENTE --")
            object_send.con = _socket

            while object_send.loop():
                with self._lock:
                    msg = _socket.recv(1024)
                    iter(self(msg))
                    next(self)
                    if not msg: break
                    print(str(msg, 'utf8'))
