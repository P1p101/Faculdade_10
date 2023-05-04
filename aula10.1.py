import time
import pyautogui

pyautogui.press('Win')
pyautogui.write('Bloco de notas')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('Oi, tudo bem')
pyautogui.hotkey('Ctrl', 's')
pyautogui.write('mensagem.txt')
pyautogui.press('enter')


