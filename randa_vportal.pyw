# -*- coding: UTF-8 -*-

import pyautogui,sys,time,string,os
import CV

screenWidth, screenHeight = pyautogui.size()
curr_path=os.path.abspath('.')+(r'\PNG')

def login(userid,userpw):
    pyautogui.hotkey('win','4',interval=2.25)  #open chrome
    time.sleep(3)
    pyautogui.hotkey('ctrl','2',interval=4.25) # switch abs
    time.sleep(3)
    #x1=0.9585
    #y1=0.8870
    #pyautogui.click(screenWidth*x1,screenHeight*y1,button='left') # username
    userlocation = pyautogui.locateOnScreen(curr_path+r'\abs_user.png')         #这个是成功的
    buttonx, buttony = pyautogui.center(userlocation)
    pyautogui.doubleClick(buttonx,buttony) # username
    pyautogui.hotkey('end')         # end
    for i in range(1,20):
        pyautogui.hotkey('backspace')         # bkspace
    pyautogui.typewrite(userid,interval=0.5)
    pyautogui.hotkey('tab',interval=0.5)
    pyautogui.typewrite(userpw,interval=0.5)
    pyautogui.hotkey('enter',interval=2.25)

def logout():
    x1=0.81445
    y1=0.0795
    pyautogui.click(screenWidth*x1,screenHeight*y1,button='left')
    pyautogui.hotkey('enter',interval=1.5)

def switch_company(div):
    x=float(1647)/1920
    y=float(112)/1080
    userlocation = pyautogui.locateOnScreen(curr_path+r'\logo_1080.png')
    if userlocation:
        buttonx, buttony = pyautogui.center(userlocation)
    else:
        buttony=screenHeight*y
    buttonx=screenWidth*x
    pyautogui.click(buttonx,buttony,button='left',interval=0.5)
    time.sleep(2)
    dict_co={'0111':2,'0511':3,'0512':4,'0513':5,'0712':6,'0812':7}
    curr_int=int(dict_co[div])
    for i in range(1,curr_int):
        pyautogui.hotkey('down',interval=1.5)
    pyautogui.hotkey('enter',interval=1.5)

def cm18():
    x1=float(99)/1920
    y1=float(137)/1080
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
    x1=float(99)/1920
    y1=float(137)/1080
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
    x=float(99)/1920
    y=float(137)/1080
    userlocation = pyautogui.locateOnScreen(curr_path+r'\abs_command.png')
    if userlocation:
        buttonx, buttony = pyautogui.center(userlocation)
    else:
        buttonx=screenWidth*x
        buttony=screenHeight*y
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
    sold=a1.replace('*','')
    pyautogui.press('tab',interval=1.5)
    time.sleep(0.5)
    pyautogui.typewrite(sold,interval=0.5)
    if len(sold)<7:
        pyautogui.press('tab',interval=0.5)
    pyautogui.typewrite(d1,interval=0.5)
    pyautogui.typewrite(d2,interval=0.5)
    if p1=='All':
        pass
    else:
        for i in range(3):
            pyautogui.press('tab',interval=0.5)
        pyautogui.typewrite(p1,interval=0.5)
    pyautogui.hotkey('enter',interval=1)
    time.sleep(3)                                                   # press enter we have to wait
    if a1==sold:
        pass
    else:
        icount=len(a1)-len(sold)
        for  i in range(icount):
            time.sleep(2)
    pyautogui.click(screenWidth/2,screenHeight/2,button='left')
    pyautogui.hotkey('ctrl','a',interval=0.25)
    pyautogui.hotkey('ctrl','c',interval=0.25)
    str1=CV.gettext()
    pyautogui.press('tab',interval=1.5)
    condition_list=[]
    condition_list.append("{:0>7d}".format(int(sold)))
    condition_list.append(d1)
    condition_list.append(d2)
    condition_list.append(p1)
    return condition_list,str1


if __name__=="__main__":
    login(sys.argv[1].lower(),sys.argv[2].upper())
