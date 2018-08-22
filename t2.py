# -*- coding: GBK -*-

import pyautogui,time

screenWidth, screenHeight = pyautogui.size() # 屏幕尺寸

mouseX, mouseY = pyautogui.position() # 返回当前鼠标位置，注意坐标系统中左上方是(0, 0)

print (" X coefficient:", float(mouseX)/screenWidth)

print (" Y coefficient:", float(mouseY)/screenHeight)

print screenWidth

print screenHeight

print mouseX

print mouseY
