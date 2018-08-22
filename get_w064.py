# -*- coding: GBK -*-

import pyautogui,sys,string,time,re
import randa_vportal,CV


#get parameters

result=[]
with open('w064_para.txt', 'r') as f:
    for line in f:
        result.append(line.strip('\n'))

first_row=result.index('list_date')
last_row=result.index('--end')
d1_list=result[int(first_row)+1:int(last_row)]
del result[last_row]

first_row=result.index('list_account')
last_row=result.index('--end')
a1_list=result[first_row+1:last_row]
del result[last_row]
str1=';'.join(a1_list)
str1=str1.replace('(','')
str1=str1.replace(')','')
a1_list=str1.split(';')

first_row=result.index('list_product')
last_row=result.index('--end')
p1_list=result[first_row+1:last_row]
del result[last_row]

# 打开写入的文件
name_str='W064_result_'+ str(time.strftime("%m%d%H%M",time.localtime()))+'.csv'
f = open(name_str, 'w')
f.write('From_date;To_date;Product;Sold#;Items;Amount;Invalid;No\n')



# 用来拆分字符串的自定义函数,最终输出一个字典
def split_order_fulfilment(str1):
    str2=re.findall(r"\--+(.+?)\+F3=Exit",str1)
    str3=str2[0]
    op_result=re.findall(r'[A-Z\>][a-zA-Z\s\(]{1,30}\s[\d]{1,9}',str3)
    new_list=[]
    list2=[]
    for op in op_result:
        templist=re.findall(r'[A-Z\>\(][A-Za-z\(]+',op)
        if len(templist)==1:
            new_list.extend(templist)
        elif len(templist)>1:
            str4=' '.join(templist)
            new_list.append(str4)
        list2.extend(re.findall(r'[\d]{1,9}$',op))
    return str3,new_list,list2

screenWidth, screenHeight = pyautogui.size() # 屏幕尺寸
randa_vportal.login(sys.argv[1].lower(),sys.argv[2].upper())
time.sleep(3)
pyautogui.hotkey('enter',interval=0.25)
time.sleep(3)
randa_vportal.switch_company_0712()
time.sleep(2)
i=0
find_ix=0
last_str=''
randa_vportal.enter_w064(i)
for p1 in p1_list:
    i +=1
    time.sleep(1)
    for a1 in a1_list:        
        str1=randa_vportal.W064(a1,d1_list[0],d1_list[1],p1)
        this_str,list1,list2=split_order_fulfilment(str1)
        t=0      
        for line_out in list1:
            str2=d1_list[0]+';'+d1_list[1]+';'+ p1+';'+a1+';'+line_out+';'+list2[t]
            if this_str<>last_str:
                str2=str2+';;' + str(find_ix)
            else:
                str2=str2+';confirm_repeat;' + str(find_ix)
            f.write(str2+'\n')
            t +=1
        find_ix +=1
        last_str=this_str
        time.sleep(1)        
f.close()
    
    
