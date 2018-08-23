# -*- coding: UTF-8 -*-

import pyautogui,sys,time,string,os
import CV

screenWidth, screenHeight = pyautogui.size() # 获取屏幕尺寸
curr_path=os.path.abspath('.')+(r'\PNG')

def login(userid,userpw):
    pyautogui.hotkey('win','4',interval=2.25)  #open chrome
    time.sleep(3)
    pyautogui.hotkey('ctrl','2',interval=4.25) # switch abs
    time.sleep(3)
    #x1=0.9585
    #y1=0.8870
    #pyautogui.click(screenWidth*x1,screenHeight*y1,button='left') # username
    userlocation = pyautogui.locateOnScreen(curr_path+r'\abs_user.png')
    buttonx, buttony = pyautogui.center(userlocation)
    pyautogui.doubleClick(buttonx,buttony) # username
    pyautogui.hotkey('end')         # end
    for i in range(1,12):
        pyautogui.hotkey('backspace')         # bkspace
    pyautogui.typewrite(userid,interval=0.5)
    pyautogui.hotkey('tab',interval=0.5)
    pyautogui.typewrite(userpw,interval=0.5)
    pyautogui.hotkey('enter',interval=2.25)

def logout():
    x1=0.81445
    y1=0.0795
    pyautogui.click(screenWidth*x1,screenHeight*y1,button='left') # 点击 退出
    pyautogui.hotkey('enter',interval=1.5)

def switch_company_0111():
    x=0.8914
    y=0.0777
    userlocation = pyautogui.locateOnScreen(curr_path+r'\logo.png')
    buttonx, buttony = pyautogui.center(userlocation)
    pyautogui.click(screenWidth*x,buttony,button='left',interval=0.5)
    time.sleep(2)
    for i in range(1,2):
        pyautogui.hotkey('down',interval=1.5)
    pyautogui.hotkey('enter',interval=1.5)

def switch_company_0511():
    x=0.8914
    y=0.0777
    userlocation = pyautogui.locateOnScreen(curr_path+r'\logo.png')
    buttonx, buttony = pyautogui.center(userlocation)
    pyautogui.click(screenWidth*x,buttony,button='left',interval=0.5)
    time.sleep(2)
    for i in range(1,3):
        pyautogui.hotkey('down',interval=1.5)
    pyautogui.hotkey('enter',interval=1.5)

def switch_company_0512():
    x=0.8914
    y=0.0777
    userlocation = pyautogui.locateOnScreen(curr_path+r'\logo.png')
    buttonx, buttony = pyautogui.center(userlocation)
    pyautogui.click(screenWidth*x,buttony,button='left',interval=0.5)
    time.sleep(2)
    for i in range(1,4):
        pyautogui.hotkey('down',interval=1.5)
    pyautogui.hotkey('enter',interval=1.5)

def switch_company_0513():
    x=0.8914
    y=0.0777
    userlocation = pyautogui.locateOnScreen(curr_path+r'\logo.png')
    buttonx, buttony = pyautogui.center(userlocation)
    pyautogui.click(screenWidth*x,buttony,button='left',interval=0.5)
    time.sleep(2)
    for i in range(1,5):
        pyautogui.hotkey('down',interval=1.5)
    pyautogui.hotkey('enter',interval=1.5)

def switch_company_0712():
    x=0.8914
    y=0.0777
    userlocation = pyautogui.locateOnScreen(curr_path+r'\logo.png')
    buttonx, buttony = pyautogui.center(userlocation)
    pyautogui.click(screenWidth*x,buttony,button='left',interval=0.5)
    time.sleep(2)
    for i in range(1,6):
        pyautogui.hotkey('down',interval=1.5)
    pyautogui.hotkey('enter',interval=1.5)

def switch_company_0812():
    x=0.8914
    y=0.0777
    userlocation = pyautogui.locateOnScreen(curr_path+r'\logo.png')
    buttonx, buttony = pyautogui.center(userlocation)
    pyautogui.click(screenWidth*x,buttony,button='left',interval=0.5)
    time.sleep(2)
    for i in range(1,7):
        pyautogui.hotkey('down',interval=1.5)
    pyautogui.hotkey('enter',interval=1.5)

def cm18():
    x1=0.05
    y1=0.09444
    pyautogui.click(screenWidth*x1,screenHeight*y1,button='left') # command
    pyautogui.typewrite('CM18',interval=1.5)
    pyautogui.hotkey('enter',interval=1.5)
    for i in range(1,20):
        pyautogui.hotkey('tab',interval=1.2)
    pyautogui.typewrite('C',interval=2.25)
    # save screenshot
    name_str='CM18_screenshot_'+ str(time.strftime("%m%d%H%M",time.localtime()))+'.png'
    im1 = pyautogui.screenshot(name_str)
    pyautogui.hotkey('enter',interval=1.55)

def E070(account1,wk_off=0):
    x1=0.05
    y1=0.09444
    wk1=int(time.strftime("%w",time.localtime()))+1+int(wk_off)*7
    d2=str(time.strftime("%y%m%d",time.localtime()-wk1))
    d1=str(time.strftime("%y%m%d",time.localtime()-wk1-7))
    pyautogui.click(screenWidth*x1,screenHeight*y1,button='left') # command
    pyautogui.typewrite('E070',interval=1.5)
    pyautogui.press('enter',interval=1.5)
    pyautogui.typewrite(account1,interval=1.5)
    pyautogui.press('tab',interval=1.5)
    pyautogui.typewrite('S',interval=1.5)
    pyautogui.typewrite(d1,interval=1.5)
    pyautogui.typewrite(d2,interval=1.5)
    pyautogui.press('tab',interval=1.5)
    pyautogui.press('Y',interval=1.5)
    pyautogui.press('T',interval=1.5)
    # save screenshot
    name_str='E070_screenshot_'+ str(time.strftime("%m%d%H%M",time.localtime()))+'.png'
    im1 = pyautogui.screenshot(name_str)
    pyautogui.hotkey('enter',interval=2.55)

def enter_w064(t1=0):
    userlocation = pyautogui.locateOnScreen(curr_path+r'\abs_command.png')
    buttonx, buttony = pyautogui.center(userlocation)
    pyautogui.click(buttonx,buttony,button='left') # command
    pyautogui.typewrite('W064',interval=1.5)
    time.sleep(3)
    pyautogui.hotkey('enter',interval=1.5)
    if t1>0:
        time.sleep(3)
        pyautogui.hotkey('tab',interval=1.5)
        time.sleep(1)
        pyautogui.hotkey('enter',interval=1.5)

def W064(a1,d1,d2,p1):
    #pyautogui.press('tab',interval=1.5)
    userlocation = pyautogui.locateOnScreen(curr_path+r'\w064_sold_row.png')
    buttonx, buttony = pyautogui.center(userlocation)
    pyautogui.click(buttonx,buttony,button='left',interval=0.5)
    pyautogui.typewrite(a1,interval=0.5)
    if len(a1)<7:
        pyautogui.press('tab',interval=1.5)
    pyautogui.typewrite(d1,interval=0.5)
    pyautogui.typewrite(d2,interval=0.5)
    for i in range(3):
        pyautogui.press('tab',interval=1.5)
    pyautogui.typewrite(p1,interval=0.5)
    pyautogui.hotkey('enter',interval=0.5)
    time.sleep(3)
    pyautogui.click(screenWidth/2,screenHeight/2,button='left')
    pyautogui.hotkey('ctrl','a',interval=0.25)
    time.sleep(1)
    pyautogui.hotkey('ctrl','c',interval=0.25)
    time.sleep(1)
    str1=CV.gettext()
    time.sleep(1)
    pyautogui.press('tab',interval=1.5)
    return str1


if __name__=="__main__":
    login(sys.argv[1].lower(),sys.argv[2].upper())
