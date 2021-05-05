from PySimpleGUI import PySimpleGUI as sg
import webbrowser
import pyautogui
import time 
import os
import fnmatch
import shutil

def getIn(t, loading_Time):
    
    sus = input(Digite o sus: )
    webbrowser.open('http://siga.saude.prefeitura.sp.gov.br/sms/login.do?method=logoff')

    time.sleep(loading_Time)

    print(pyautogui.position())
    pyautogui.moveTo(723, 286, duration=t)
    pyautogui.click(723, 286, button='left', duration=t)

    pyautogui.moveTo(859, 342, duration=t)
    pyautogui.click(859, 342, button='left', duration=t)

    pyautogui.moveTo(1228,369, duration=t)
    pyautogui.click(1228,369, button='left', duration=t)

    time.sleep(2*loading_Time/3)

    #RecepçãoDeUsuários
    pyautogui.moveTo(291, 183, duration=t)

    pyautogui.moveTo(315,435, duration=t)
    pyautogui.click(315,435, button='left', duration=t)


    pyautogui.moveTo(276,366, duration=t)
    pyautogui.click(276,366, button='left', duration=t)
    pyautogui.write(sus)

    #OutClick
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

    #Registro Reduzido
    pyautogui.moveTo(291, 183, duration=t)
    pyautogui.moveTo(335, 213, duration=t)
    pyautogui.click(335, 213, button='left', duration=t)

    #NovoAtendimento
    pyautogui.moveTo(1622, 556, duration=t)
    pyautogui.click(1622, 556, button='left', duration=t)
    time.sleep(2)

    #ColocaSUS
    pyautogui.moveTo(437, 440, duration=t)
    pyautogui.click(437, 440, button='left', duration=t)
    pyautogui.write(sus)

    #OutClick
    pyautogui.moveTo(1048, 394, duration=t)
    pyautogui.click(1048, 394, button='left', duration=t)

    #CancelClick
    pyautogui.moveTo(1854, 927, duration=t)
    pyautogui.click(1854, 927, button='left', duration=t)
    pyautogui.scroll(-10000)

def exit():
    pyautogui.moveTo(1818, 182, duration=0.25)
    pyautogui.click(1818, 182, button='left', duration=0.25)
    time.sleep(1)
    pyautogui.moveTo(1052, 229, duration=0.25)
    pyautogui.click(1052, 229, button='left', duration=0.25)
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
    [sg.Text('SUS         '), sg.Input(key='sus', size =(20,1) )],
    [sg.Text('Loading Time'), sg.Input(key='loading_Time', size =(20,1) )],
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
        loading_Time = int(values['loading_Time'])
        t = (100 - float(values['t']))/100
        window.hide()
        time.sleep(1)
        getIn(t, loading_Time   )
        exit()
        window.un_hide()

    if window == window2 and event == 'Exit':
        window2.hide()
        window1.un_hide()
#Logica
