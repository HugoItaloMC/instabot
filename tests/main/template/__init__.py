from queue import Queue
from itertools import islice
from typing import Coroutine

import PySimpleGUIQt as pygui
from template.main_template import MainBox
from template.tasks_template import TasksBox
__all__ = ['Template']

class Template:

    def __init__(self, schema) -> None:
        self.__schema: object = schema  # Data-classe dados recebidos através do template
        
        self.__window_tasks: 'PySimpleGUIQt.Window' = None
        self.__window_main: 'PySimpleGUIQt.Window' = None
        
    
    def __iter__(self) -> object:
        global factory, tasks 
        if self.__window_main is None:
            self.__window_main = pygui.Window('Main Menu', MainBox(gui_engine=pygui).get(), finalize=True)
        else:
            self.__window_main.close()

        while True:
            # LOCAL VAR
            queue = Queue()

            # GLOBAL VAR
            factory = None
            tasks = None

            # VERIFICANDO EVENTOS E DADOS
            event, values = self.__window_main.read()

            if event in (None, 'stop'):
                self.__window_main.close()

            # BEGIN TEMPLATE
            if event == 'start_task':
                self.__window_main.close()  # CLOSED MAIN WINDOW
                
                # ENVIANDO DADOS    
                schema: Coroutine = iter(self.__schema(Request=(values['username'], values['password'], values['path'])))
                next(schema)
                
                # BUSCANDO QUEUE
                __queue = schema.send('QUEUE')

                # RECOLHENDO REFERÊNCIAS DENTRO DA QUEUE
                while not __queue.empty():
                    factory = __queue.get()

            if factory is not None:
                # Armazenando instância da classe concret `Login` na fila principal
                queue.put(next(factory))
            

            # VERIFICANDO TAREFAS SOLICITADAS
            tasks = {key for key, _ in values.items() if type(_) is not str and _}

 
            #print(tasks)  # LOG
            
            try:
                # Iniciando corroutina para buscar tarefas solicitadas, ñ retorna nenhum valor através do ponteiro
                factory.send(bool(tasks))
                
                # Armazenando tarefas `concrets na fila`
                factory.send(tasks.copy())
                for line in range(1, len(tasks)+1):
                    queue.put(factory.send(bool(line)))
                # Tratando exceptions default de corroutinas >> `factory e schema`
            except StopIteration:
                factory.close()
                schema.close()
            except AttributeError:
                exit()
            except Exception:
                exit(2)
            
            # CLASSES `Concrets`
            Login: object = None
            Comment: object  = None
            Like: object = None
            Follow: object = None
            Unfollow: object = None

            # GET Concrets
            while not queue.empty():
                Login = queue.get()
                if 'comment' in tasks:
                    Comment = queue.get()
                if 'like' in tasks:
                    Like = queue.get()
                if 'follow' in tasks:
                    Follow = queue.get()
                if 'unfollow' in tasks:
                    Unfollow = queue.get()

                

            # BEGIN MENU TASKS
            Login.run()
            while True:

                if self.__window_tasks is None:
                    self.__window_tasks = pygui.Window('Menu Tasks', TasksBox(tasks=tasks.copy(), gui_engine=pygui).get(), finalize=True)
                    
                event, _ = self.__window_tasks.read(timeout=None)
                if event in (pygui.WIN_CLOSED, None, 'STOP'):
                    exit()
                print('\n Event: %s\n' % event, 'Concrets:\t%s' % Login, Comment, Like, Follow, Unfollow, '\n')  # LOG
                

                if event == 'start_comment':
                    Comment.run() if Comment else None
                elif event == 'start_like':
                    Like.run() if Like else None
                elif event == 'start_follow':
                    Follow.run() if Follow  else None
                elif event == 'start_unfollow':
                    Unfollow.run() if Unfollow else None
                else:
                    exit()

        return self
