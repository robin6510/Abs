# -*- coding: UTF-8 -*-

import pyautogui,sys

pyautogui.PAUSE = 0.5

if len(sys.argv)>2 :
    sys.exit(1)

cf_count=int(sys.argv[1])

 # �л����� ������������ʽ
pyautogui.hotkey('alt', 'tab')
pyautogui.press('alt')
pyautogui.press('h')
pyautogui.press('l')
pyautogui.press('r')

for i in range(1,6):
    pyautogui.hotkey('tab') # �л�

for i in range(cf_count):
    pyautogui.hotkey('alt', 'e') # edit rule
    pyautogui.hotkey('alt', 'o') # formula
    pyautogui.hotkey('enter') # enter
    pyautogui.hotkey('down') # next
