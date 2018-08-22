# -*- coding: UTF-8 -*-

import pyautogui,time

screenWidth, screenHeight = pyautogui.size() # ��Ļ�ߴ�

mouseX, mouseY = pyautogui.position() # ���ص�ǰ����λ�ã�ע������ϵͳ�����Ϸ���(0, 0)

print (" X coefficient:", float(mouseX)/screenWidth)

print (" Y coefficient:", float(mouseY)/screenHeight)

print screenWidth

print screenHeight

print mouseX

print mouseY
