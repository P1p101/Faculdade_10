import pyautogui
import time

pyautogui.press('Win')
time.sleep(2)
pyautogui.write('Google')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.position(x=1554, y=198)
pyautogui.write("www.youtube.com")
pyautogui.press('enter')