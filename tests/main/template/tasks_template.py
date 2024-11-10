

class TasksBox:

    def __init__(self, tasks: set, gui_engine: 'PySimpleGUIQt') -> None:
        self.__tasks = tasks
        self.__gui_engine = gui_engine
        self.__dynamic_layout: list = []
        self.__dynamic_layout.append([self.__gui_engine.Text('TASKs Menu', font=('Goto', 15), justification='center')])
        for task in self.__tasks:
            self.__dynamic_layout.append([self.__gui_engine.Stretch(key=None),
            self.__gui_engine.Button('start task %s' % task, key='start_%s' % task, size=(len(task)+5, 1)),
            self.__gui_engine.Stretch(key=None)])
        
        self.__dynamic_layout.append([self.__gui_engine.Stretch(key=None), self.__gui_engine.Button('STOP')])

    def get(self) -> list:
        return self.__dynamic_layout


