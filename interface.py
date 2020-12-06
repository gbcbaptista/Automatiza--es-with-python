from PySimpleGUI import PySimpleGUI as sg

#Criar windows
def window_login():
    sg.theme('reddit')
    layout = [
    [sg.Text('Usuário'), sg.Input(key='user', size =(20,1) )],
    [sg.Text('Senha  '), sg.Input(key='password', password_char='*', size =(20,1) )],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
    ]
    return sg.Window('Login', layout, finalize=True)

def window_menu():
    sg.theme('reddit')
    layout = [
    [sg.Button('Dar Baixa'), sg.Button('Exit')]
    ]

    return sg.Window('Menu', layout, finalize=True)
#Create Start windows
window1, window2 = window_login(), None

#Criar loop
while True:
    window, event, values = sg.read_all_windows()
    #When the window be closed
    if window == window1 and event == sg.WIN_CLOSED:
        break


    #When we want go for next window
    if window == window1 and event == 'Entrar':
        if values['user'] == 'gbc123' and values['password'] == '123':
            window1.hide()
            window2 = window_menu()
        
    #When we want back to the previous window
    if window == window2 and event == 'Dar Baixa':
        window.hide()
        time.sleep(1)
        getIn()
        window.un_hide()

    if window == window2 and event == 'Exit':
        window2.hide()
        window1.un_hide()
#Logica