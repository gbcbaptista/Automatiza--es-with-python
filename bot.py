from PySimpleGUI import PySimpleGUI as sg
import webbrowser
import pyautogui
import time 
import os
import fnmatch
import shutil

def getIn():
    webbrowser.open('http://siga.saude.prefeitura.sp.gov.br/sms/login.do?method=logoff')

    time.sleep(5)

    print(pyautogui.position())
    pyautogui.moveTo(723, 286, duration=0.25)
    pyautogui.click(723, 286, button='left', duration=0.25)

    pyautogui.moveTo(859, 342, duration=0.25)
    pyautogui.click(859, 342, button='left', duration=0.25)

    pyautogui.moveTo(1228,369, duration=0.25)
    pyautogui.click(1228,369, button='left', duration=0.25)

    time.sleep(3)

    #Atender
    pyautogui.moveTo(291, 183, duration=0.25)

    pyautogui.moveTo(315,435, duration=0.25)
    pyautogui.click(315,435, button='left', duration=0.25)

    pyautogui.moveTo(276,366, duration=0.25)
    pyautogui.click(276,366, button='left', duration=0.25)
    pyautogui.write('835503012820395')

    pyautogui.moveTo(877, 331, duration=0.25)
    pyautogui.click(877, 331, button='left', duration=0.25)

    #Consultar
    pyautogui.moveTo(1749,527, duration=0.25)
    pyautogui.click(1749,527, button='left', duration=0.25)

    #Atender
    pyautogui.moveTo(1753, 665, duration=0.25)
    pyautogui.click(1753, 665, button='left', duration=0.25)

    #Não
    time.sleep(1)
    pyautogui.moveTo(1033, 635, duration=0.25)
    pyautogui.click(1033, 635, button='left', duration=0.25)

    #Sair
    pyautogui.moveTo(1818, 182, duration=0.25)
    pyautogui.click(1818, 182, button='left', duration=0.25)
    time.sleep(1)
    pyautogui.moveTo(1052, 229, duration=0.25)
    pyautogui.click(1052, 229, button='left', duration=0.25)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')

#Layout
sg.theme('reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='user', size =(20,1) )],
    [sg.Text('Senha  '), sg.Input(key='password', password_char='*', size =(20,1) )],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]
#Janela
window = sg.Window('Tela de Login', layout)
#Ler Eventos
while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Entrar':
        if values['user'] == 'gbc123' and values['password'] == '123':
            window.close()
            time.sleep(1)
            getIn()