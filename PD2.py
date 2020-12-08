from PySimpleGUI import PySimpleGUI as sg
import webbrowser
import pyautogui
import time 
import os
import fnmatch
import shutil
import datetime

time.sleep(2)

loadin_Time = 2
t = 0.25

#mudando nome do arquivo
pyautogui.hotkey('win', 'e')
pyautogui.hotkey('f11')
pyautogui.moveTo(670, 21, duration = 0.25)
pyautogui.click(670, 21, duration = 0.1)
pyautogui.write(r"C:\Users\gbcba\Downloads")
pyautogui.press('enter')



time.sleep(1)

pyautogui.moveTo(670, 800, duration = 0.1)
pyautogui.click(670, 800, duration = 0.1)

#Mudando Nome do Arquivo
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('f2')
time.sleep(1)
pyautogui.hotkey('f2')
time.sleep(1)


#Digitando Nome
pyautogui.write('DadosUPA')
pyautogui.press('enter')
pyautogui.hotkey('f11')
time.sleep(1)
pyautogui.hotkey('alt', 'f4')

time.sleep(1)


webbrowser.open('https://colab.research.google.com/drive/1WcghE2RcziGRU5DQtODdbXPOzby__A3V?authuser=2')

time.sleep(10)


#Step1 Google Colab
pyautogui.moveTo(98, 310, duration = t)
pyautogui.click(98, 310, duration = t)
time.sleep(10)

#Fazendo Upload
pyautogui.moveTo(229, 375, duration = t)
pyautogui.click(229, 375, duration = t)
time.sleep(10)


#Escrevendo Path
pyautogui.moveTo(448, 63, duration = t)
pyautogui.click(448, 63, duration = t)
pyautogui.write(r"C:\Users\gbcba\Downloads")
pyautogui.press('enter')


#Escrevendo Nome do Arquivo
pyautogui.moveTo(444, 521, duration = t)
pyautogui.click(444, 521, duration = t)
pyautogui.write('DadosUPA.xls')

#Abrindo Upload
pyautogui.moveTo(742, 560, duration = t)
pyautogui.click(742, 560, duration = t)


#Step2 Google Colab


# Abrindo Geral e Copiando

# Abrindo Gráfico e Colando

# Arbindo Clínica e Copiando

# Colando em Gráfico

# Desproteger Planilha

# Mudar Data

# Proteger Planilha

# Salvar