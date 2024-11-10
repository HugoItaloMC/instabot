
class MainBox:

    def __init__(self, gui_engine):
        self.__gui_engine = gui_engine
        self.__LAYOUT: list = [
        [self.__gui_engine.Stretch(key=None),self.__gui_engine.Text("INSTABOT\nTool", size=(60, 2), font=("Goto", 20), justification='center'), self.__gui_engine.Stretch(key=None)],
        [self.__gui_engine.Text('_' * 80, justification='center')],
        [self.__gui_engine.Text("Your username and password Instagram:", font=("Goto", 15), justification='center')],
        
        [self.__gui_engine.Stretch(key=None), self.__gui_engine.Text('User:', size=(5, 1)),
        self.__gui_engine.InputText(key='username', justification='center',size=(10, 1)),
        self.__gui_engine.Text('Pass', size=(6, 1), justification='center'),
        self.__gui_engine.InputText(justification='center',size=(10, 1), key='password', password_char='*'), self.__gui_engine.Stretch(key=None)],
        [self.__gui_engine.Text('=' * 80, justification='center')
        ],
        
        [self.__gui_engine.Text("TASKS", justification='center', font=("Goto", 15))],
        [self.__gui_engine.Text("_" * 80, justification='center')],
        
        [self.__gui_engine.Stretch(key=None),self.__gui_engine.Checkbox('LIKE', font=("Sans-serif", 10), key='like'),
        self.__gui_engine.Checkbox('COMMENT', font=("Sans-serif", 10), key='comment'),
        self.__gui_engine.Checkbox('FOLLOW', font=("Sans-serif", 10), key='follow'),
        self.__gui_engine.Checkbox('UNFOLLOW', font=("Sans-serif", 10), key='unfollow'), self.__gui_engine.Stretch(key=None)],
        [self.__gui_engine.Text('_' * 80, justification='center')
        ],
        [self.__gui_engine.Text('Open file with users to do tasks (like, comment, follow, unfollow)\nsupport files: (*.json, *.csv, *.xlsx)', justification='center')],
        [self.__gui_engine.Stretch(key='clear'),self.__gui_engine.Text("Open file", size=(10, 1), auto_size_text=False, font=("Goto", 15)), 
        self.__gui_engine.InputText("path to file", key='path', justification='left', size=(30, 1), font=("Goto", 15)), 
        self.__gui_engine.FileBrowse(file_types=(('JSON', '*.json'), ("EXCEL", "*.xlsx"), ("CSV", "*.csv"))), self.__gui_engine.Stretch(key=None)],
        [self.__gui_engine.Stretch(key=None), self.__gui_engine.Button('start', size=(100, 30), key='start_task'), self.__gui_engine.Button('stop', size=(100, 30), key='stop'), self.__gui_engine.Stretch(key=None)],
        ]
    
    def get(self) -> list:
        return self.__LAYOUT
         