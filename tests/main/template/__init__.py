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
        global factory, tasks, Login, Like, Comment, Follow, Unfollow
        if self.__window_main is None:
            self.__window_main = pygui.Window('Main Menu', MainBox(gui_engine=pygui).get(), finalize=True)
        else:
            self.__window_main.close()

        while True:
            # GLOBAL VAR
            factory = None
            tasks = None

            # CLASSES `Concrets`
            Login = None
            Comment  = None
            Like = None
            Follow = None
            Unfollow = None

            # VERIFICANDO EVENTOS E DADOS
            event, values = self.__window_main.read()

            if event in (None, 'stop'):
                self.__window_main.close()

            # BEGIN TEMPLATE
            if event == 'start_task':
                self.__window_main.close()  # CLOSED MAIN WINDOW
                
                # ENVIANDO DADOS    
                schema: Coroutine = iter(self.__schema(Request=(values['username'], values['password'], values['path'])))
                # BUSCANDO FACTORY
                factory = next(schema)

            if factory is not None:
                next(factory)

            tasks = {key for key, _ in values.items() if type(_) is not str and _}
            try:
                #print(tasks)  # LOG
                Login = factory.send(bool(tasks))
                Comment = factory.send(bool(Login))
                Like = factory.send(bool(Comment))
                Follow = factory.send(bool(Like))
                Unfollow = factory.send(bool(Follow))
            except RuntimeError:
                factory.close()
                schema.close()
            except Exception:
                exit(2)
                
            
            # BEGIN MENU TASKS
            Login.run()
            while True:

                if self.__window_tasks is None:
                    self.__window_tasks = pygui.Window('Menu Tasks', TasksBox(tasks=tasks.copy(), gui_engine=pygui).get(), finalize=True)
                    
                event, _ = self.__window_tasks.read(timeout=None)
                if event in (pygui.WIN_CLOSED, None, 'STOP'):
                    return
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
