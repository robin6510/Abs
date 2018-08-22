# -*- coding: GBK -*-

import pyautogui,randa_vportal,sys,string,time 


randa_vportal.login(sys.argv[1].lower(),sys.argv[2].upper())

time.sleep(3)

pyautogui.hotkey('enter',interval=0.25)

time.sleep(3)

randa_vportal.switch_company_0111()
randa_vportal.cm18()

randa_vportal.switch_company_0511()
randa_vportal.cm18()

randa_vportal.switch_company_0512()
randa_vportal.cm18()

randa_vportal.switch_company_0712()
randa_vportal.cm18()

randa_vportal.switch_company_0812()
randa_vportal.cm18()

randa_vportal.logout()




