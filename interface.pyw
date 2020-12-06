from PySimpleGUI import PySimpleGUI as sg
import webbrowser
import pyautogui
import time 
import os
import fnmatch
import shutil

def getIn(t):
    webbrowser.open('http://siga.saude.prefeitura.sp.gov.br/sms/login.do?method=logoff')

    time.sleep(5)

    print(pyautogui.position())
    pyautogui.moveTo(723, 286, duration=t)
    pyautogui.click(723, 286, button='left', duration=t)

    pyautogui.moveTo(859, 342, duration=t)
    pyautogui.click(859, 342, button='left', duration=t)

    pyautogui.moveTo(1228,369, duration=t)
    pyautogui.click(1228,369, button='left', duration=t)

    time.sleep(3)

    #Atender
    pyautogui.moveTo(291, 183, duration=t)

    pyautogui.moveTo(315,435, duration=t)
    pyautogui.click(315,435, button='left', duration=t)

    pyautogui.moveTo(276,366, duration=t)
    pyautogui.click(276,366, button='left', duration=t)
    pyautogui.write('835503012820395')

    pyautogui.moveTo(877, 331, duration=t)
    pyautogui.click(877, 331, button='left', duration=t)


    pyautogui.moveTo(1749,527, duration=t)
    pyautogui.click(1749,527, button='left', duration=t)

    #Atender
    pyautogui.moveTo(1753, 665, duration=t)
    pyautogui.click(1753, 665, button='left', duration=t)

    #Não
    time.sleep(1)
    pyautogui.moveTo(1033, 635, duration=t)
    pyautogui.click(1033, 635, button='left', duration=t)

    #Sair
    pyautogui.moveTo(1818, 182, duration=t)
    pyautogui.click(1818, 182, button='left', duration=t)
    time.sleep(1)
    pyautogui.moveTo(1052, 229, duration=t)
    pyautogui.click(1052, 229, button='left', duration=t)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')

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
    #[sg.Checkbox()],
    [sg.Slider(key='t', range=(1,100), default_value=75, size=(20,15), orientation='horizontal')],
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
    if window == window2 and event == sg.WIN_CLOSED:
        break

    #When we want go for next window
    if window == window1 and event == 'Entrar':
        if values['user'] == 'gbc123' and values['password'] == '123':
            window1.hide()
            window2 = window_menu()
        
    #When we want back to the previous window
    if window == window2 and event == 'Dar Baixa':
        t = (100 - float(values['t']))/100
        window.hide()
        time.sleep(1)
        getIn(t)
        window.un_hide()

    if window == window2 and event == 'Exit':
        window2.hide()
        window1.un_hide()
#Logica