# CLIENT (envia requisicões para `FACADE`)


# BIBLIOTECAS PADRÕES PYTHON

from collections import namedtuple
from itertools import islice
from typing import Iterator, Generator, Tuple

# IMPORTANDO BOT
from __init__ import InstaDriver


# OPERACÕES PERMITIDAS (PIPELINES)
OPERATIONS_ALLOWERS = ("LOGIN", "LIKE", "FOLLOW", "UNFOLLOW", "COMMENT")


class Schema:

    # RECEBE ARGUMENTOS ANALISA E DIRECIONA OPERACÃO DEFINIDA
    def __init__(self, data: Tuple):
        self.data = data


    def __iter__(self):

        Request = namedtuple("Request", ("operation", "data")) # ESTRUTURA DA REQUISICÃO ENTRE OBJETOS
        
        send = yield
        if send:  # VERIFICANDO CONTRATO EXTERNO
            option = (request for request in Request(operation=send.upper(), data=self.data))
            pipe = self.__logic(args=option)
            send = yield
            if "SET" in send:
                yield self.__labor(class_=pipe)


    def __logic(self, args: Generator):
        # RECEBE DADOS E DIRECIONA OPERACÃO PARA SER REALIZADA

        op = next(args)  # VERIFICANDO OPERACÃO

        truth = True if  op in OPERATIONS_ALLOWERS else None
        if truth is not None:
            data =  args.send(truth)  # RECOLHENDO DADOS

            if op in OPERATIONS_ALLOWERS:
                print("OPERATION ON:\t%s" % op)
                pipe_insta = InstaDriver(data=data, operation=op)
                return pipe_insta


    def __labor(self, class_):
        # EXECUTA A OPERACÃO DEFINIDA
        xiter_class = islice(class_, None)  # chamando __iter__ de `class_`
        idx = next(xiter_class)  # CHAMANDO `__next__` de `class_`
        return idx


if __name__ == '__main__':
    import sys
    import argparse
    from time import sleep

    # ESTRUTURANDO DADOS RECEBIDOS
    Data = namedtuple("Data", ("username", "passwd", "path"))

    # ANALISANDO ARGUMENTOS(dados) PASSADOS POR LINHA DE COMANDO
    args = argparse.ArgumentParser(sys.argv[1:], description="ARGS OF CLIENT SEND FROM INTERFACE")
    args.add_argument("--username", "-l",type=str, required=True, help="Username login instagram")
    args.add_argument("--passwd", "-p",type=str, required=True, help="Passwd login instagram")
    args.add_argument("--path", type=str, required=True, help="Path file users to manager")
    args.add_argument("--login", action="store_true", required=True, help="CONSTRAING APLICATION")
    args.add_argument("--operation", "-op", type=str, required=True)
    namespaces = args.parse_args()
    
    login = namespaces.login
        
    try:
        if namespaces.login:
            data = Data(username=namespaces.username, passwd=namespaces.passwd, path=namespaces.path)
        
            schema = iter(Schema(data=data))
            next(schema)
            schema.send(namespaces.operation)
            sleep(1)
            schema.send("SET")
        else:
            # LOG ERROR
            print("## Error ##\tFLAG `--login` IS NECESSARY")

    except StopIteration:
        schema.close()

