import PySimpleGUIQt as pygui

LAYOUT_GUI = [
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
    [pygui.Stretch(), pygui.Button('start', size=(100, 30)), pygui.Button('stop', size=(100, 30)), pygui.Stretch()],
    [pygui.Text('_' * 60, justification='center')],
    [pygui.Stretch(), pygui.Multiline(size=(50, 10), key='status', disabled=True, autoscroll=True), pygui.Stretch()]
    ]


if __name__ == '__main__':
    window = pygui.Window(title="Tool Driver Browser", size=(640, 480), layout=LAYOUT_GUI)
    
    while True:
        button, values = window.read(timeout=100)
        if button in (pygui.WIN_CLOSED, 'Sair'):
            print("event=%s\nvalues=%s" % (button, values))
            break
        
        if 'start' in button:
            window['status'].update('Bot Iniciado')
            print('event=%s\nvalues=%s' % (button, values))
            pass
        elif 'stop' in button:
            window['status'].update('Bot Parado')
            print('event=%s\nvalues=%s' % (button, values))
            pass

    window.close()