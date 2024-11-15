

class TasksBox:

    def __init__(self, tasks: set, gui_engine: 'PySimpleGUIQt', users: set) -> None:
        self.__users: set = users
        self.__tasks = tasks
        self.__gui_engine = gui_engine
        self.__dynamic_layout: list = []
        self.__dynamic_layout.append([self.__gui_engine.Text('Tasks Menu', font=('Goto', 15), justification='center')])

        
        for task in self.__tasks:
            self.__dynamic_layout.append([self.__gui_engine.Stretch(key=None),
            self.__gui_engine.Button('start task %s' % task, key='start_%s' % task, size=(len(task)+5, 1)),
            self.__gui_engine.Stretch(key=None)])
        else:
            self.__dynamic_layout.append([self.__gui_engine.Stretch(), self.__gui_engine.Text("Users to tasks: ", font=("Goto", 12), justification='center')])
            
            self.__dynamic_layout.append([self.__gui_engine.Stretch(), self.__gui_engine.Multiline(default_text="\n".join(self.__users), size=(15, 5), key="users_tasks", disabled=False),
                                        self.__gui_engine.Stretch()])
        
        self.__dynamic_layout.append([self.__gui_engine.Stretch(key=None), self.__gui_engine.Button('STOP')])


    def get(self) -> list:
        return self.__dynamic_layout
