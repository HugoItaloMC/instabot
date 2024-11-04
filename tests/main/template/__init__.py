import PySimpleGUIQt as pygui

class Template:

    def __init__(self, schema):
        self.__schema: object = schema
        self.__window = pygui.FlexForm(title='THE SIMPLE GUI', size=(640, 480))
        self.__LAYOUT: list = [
    [pygui.Stretch(),pygui.Text("INSTABOT\nTool", size=(60, 2), font=("Goto", 20), justification='center'), pygui.Stretch()],
    [pygui.Text('_' * 80, justification='center')],
    [pygui.Text("Your username and password Instagram:", font=("Goto", 15), justification='center')],
    [pygui.Stretch(), pygui.Text('User:', size=(5, 1)),
    pygui.InputText(key='username', justification='center',size=(10, 1)),
    pygui.Text('Pass', size=(6, 1), justification='center'),
    pygui.InputText(justification='center',size=(10, 1), key='password', password_char='*'), pygui.Stretch()],
    [pygui.Text('=' * 80, justification='center')],
    [pygui.Text("TASKS", justification='center', font=("Goto", 15))],
    [pygui.Text("_" * 80, justification='center')],
    [pygui.Stretch(),pygui.Checkbox('LIKE', font=("Sans-serif", 10), key='like'),
    pygui.Checkbox('COMMENT', font=("Sans-serif", 10), key='comment'),
    pygui.Checkbox('FOLLOW', font=("Sans-serif", 10), key='follow'),
    pygui.Checkbox('UNFOLLOW', font=("Sans-serif", 10), key='unfollow'), pygui.Stretch()],
    [pygui.Text('_' * 80, justification='center')],
    [pygui.Text('Open file with users to do tasks (like, comment, follow, unfollow)\nsupport files: (*.json, *.csv, *.xlsx)', justification='center')],
    [pygui.Stretch(),pygui.Text("Open file", size=(10, 1), auto_size_text=False, font=("Goto", 15)), 
    pygui.InputText("path to file", key='path', justification='left', size=(30, 1), font=("Goto", 15)), 
    pygui.FileBrowse(file_types=(('JSON', '*.json'), ("EXCEL", "*.xlsx"), ("CSV", "*.csv"))), pygui.Stretch()],
    [pygui.Stretch(), pygui.Button('start', size=(100, 30), key='start_task'), pygui.Button('stop', size=(100, 30)), pygui.Stretch()],
    [pygui.Text('_' * 60, justification='center')],
    [pygui.Stretch(), pygui.Multiline(size=(50, 10), key='status', disabled=True, autoscroll=True), pygui.Stretch()]
    ]
    
    def __iter__(self):
        # GLOBAL VAR
        global factory, login, like, comment, follow, unfollow
        factory = None
        login = None
        like = None
        comment = None
        follow = None
        unfollow = None

        self.__window.Layout(self.__LAYOUT)
        while True:
            event, values = self.__window.read()

            if event in (None, 'Exit'):
                exit()

            if event == 'start_task':

                schema = iter(self.__schema(Request=(values['username'], values['password'], values['path'])))
                next(schema)
                queue = schema.send('DISPATCH')
                schema.close()

                while not queue.empty():
                    factory = queue.get()
                    
            if factory is not None:
                next(factory)

            login = factory.send({key for key, _ in values.items() if type(_) is not str and _})  # Default
            comment = factory.send('comment')
            like = factory.send('like')
            follow = factory.send('follow')
            unfollow = factory.send('unfollow')
        
            print(login, comment._state, like._state, follow._state, unfollow._state)
            
        self.__window.close()
        return self

if __name__ == '__main__':
    print(iter(FrontEnd()))