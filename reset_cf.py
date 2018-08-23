# -*- coding: UTF-8 -*-

import pyautogui
import sys

pyautogui.PAUSE = 0.5

if len(sys.argv)>2 :
    sys.exit(1)

cf_count=int(sys.argv[1])+1


pyautogui.hotkey('alt', 'tab')  # 切换窗口

#默认当前已经是调用条件格式的内置窗口

for i in range(1,6):
    pyautogui.hotkey('tab') # 切换
    
for i in range(1,cf_count):
    execfile("F:\Python27\USER_CODE\single_step_cf.py")
