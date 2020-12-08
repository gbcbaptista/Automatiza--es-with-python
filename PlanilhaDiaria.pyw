from PySimpleGUI import PySimpleGUI as sg
import webbrowser
import pyautogui
import time 
import os
import fnmatch
import shutil
import datetime

loadin_Time = 2
t = 0.25
webbrowser.open('http://10.41.227.240/pep/Login.aspx')
time.sleep(loadin_Time)

#Login
pyautogui.moveTo(635, 554, duration = t)
pyautogui.click(635, 554, duration = t)

#LoginSalvo
pyautogui.moveTo(635, 600, duration = t)
pyautogui.click(635, 600, duration = t)

#Logar
pyautogui.moveTo(733, 626, duration = t)
pyautogui.click(733, 626, duration = t)

time.sleep(loadin_Time)

#Ir Para Relatórios
pyautogui.moveTo(34, 509, duration = t)
pyautogui.scroll(-10000)
pyautogui.click(34, 509, duration = t)

time.sleep(loadin_Time)

#Visualizar Relatórios
pyautogui.moveTo(900, 336, duration = t)
pyautogui.click(900, 336, duration = t)

#Relátorio de Atendimentos
pyautogui.moveTo(564, 324, duration = t)
pyautogui.click(564, 324, duration = t)

#Relátorio - ATENDIMENTOS MÉDICOS
pyautogui.moveTo(218, 410, duration = t)
pyautogui.click(218, 410, duration = t)

time.sleep(loadin_Time/2)
#Selecionando DATA
pyautogui.moveTo(676, 285, duration = t)
pyautogui.click(676, 285, duration = t)
dataHoje = datetime.datetime.now() - datetime.timedelta(days=1)
pyautogui.write(str(dataHoje.strftime("%d/%m/%y")))

pyautogui.moveTo(818, 285, duration = t)
pyautogui.click(818, 285, duration = t)
pyautogui.write(str(dataHoje.strftime("%d/%m/%y")))

#To Excel
pyautogui.moveTo(1287, 295, duration = t)
pyautogui.click(1287, 295, duration = t)