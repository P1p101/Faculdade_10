import pyautogui
import time

texto = input('Digite o texto que deseja automatizar: ')
tempo = float(input('Digite o intervalo de tempo(em segundos): '))

pyautogui.hotkey('win', 'r')
pyautogui.typewrite('notepad\n')
time.sleep(2)
pyautogui.typewrite(texto, interval=tempo)