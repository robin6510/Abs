# -*- coding: UTF-8 -*-

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

# ����Ҫ��ʱ��������csv �ı��ļ�
name_str='W064_result_'+ str(time.strftime("%m%d%H%M",time.localtime()))+'.csv'
f = open(name_str, 'w')
f.write('From_date;To_date;Product;Sold#;Items;Amount_Ori;Invalid;No;Amount_Adj;Fill_Rpt\n')

# ��������ַ������Զ��庯��,�������3������ : ��ȡ�� ��ԭ�ַ���, �б�1 ,  �б� 2
def split_order_fulfilment(str1):
    str2=re.findall(r"\--+(.+?)\F3=Exit",str1)
    new_list=[]
    list2=[]
    check_list=[]
    str3=''
    if len(str2)>0:
        str3=str2[0]
        op_result=re.findall(r'[A-Z\>][a-zA-Z\s\(]{1,30}\s[\d]{1,9}',str3)
        for op in op_result:
            templist=re.findall(r'[A-Z\>\(][A-Za-z\(]+',op)
            if len(templist)==1:
                new_list.extend(templist)
            elif len(templist)>1:
                str4=' '.join(templist)
                new_list.append(str4)
            list2.extend(re.findall(r'[\d]{1,9}$',op))
    # ��ȡ��������, ����sold# ,����date, product
        op_check=str1.replace(str3,'')
    #��ȡsold# �����
        str2=re.findall(r'Sold#\d{7}',op_check)
        str5=str2[0]
        check_list.append(str5.replace('Sold#',''))
        #��ȡdate�����
        str2=re.findall(r'Start Ship Date From\s*[\d\/+]{6,8}To [\d\/+]{6,8}',op_check)
        str5=str2[0].replace('Start Ship Date From','')
        str5=str5.replace('To','').replace('/','').replace(' ','0')
        check_list.append(str5[0:6])
        check_list.append(str5[6:12])
        #��ȡproduct �����
        str2=re.findall(r'Product.+Only Div',op_check)
        str5=str2[0].replace('Product....:','').replace('Only Div','').replace(' ','')
        if str5[0]=='*':
            str5=str5.replace('*','')
        check_list.append(str5[0:3])
    else:
        pass
    return check_list,str3,new_list,list2

# ������
if sys.argv[1]=="-G":
    pyautogui.hotkey('win','4',interval=1.5)  #open chrome
    time.sleep(3)
else:
    screenWidth, screenHeight = pyautogui.size() # ��Ļ�ߴ�
    randa_vportal.login(sys.argv[1].lower(),sys.argv[2].upper())
    time.sleep(2)
    pyautogui.hotkey('enter',interval=0.25)
    time.sleep(2)
    randa_vportal.switch_company('0712')
    time.sleep(1)
    randa_vportal.enter_w064(i)
i=0
find_ix=0
last_str=''

for p1 in p1_list:
    i +=1
    sold_list=[]
    sold_list.extend(a1_list)
    for a1 in sold_list:
        condi_list,str1=randa_vportal.W064(a1,d1_list[0],d1_list[1],p1)
        check_list,this_str,list1,list2=split_order_fulfilment(str1)
        list3=[]
        for chk in list2:
            if chk>list2[0]:
                list3.append(chk[:-3])
            else:
                list3.append(chk)
        if cmp(condi_list,check_list)==0:
            t=0
            for line_out in list1:
                str2=d1_list[0]+';'+d1_list[1]+';'+ p1+';'+a1+';'+line_out+';'+list2[t]
                if this_str!=last_str:
                    str2=str2+';;' + str(find_ix)+';'+list3[t]+';'
                else:
                    str2=str2+';confirm_repeat;' + str(find_ix)+list3[t]+';'
                f.write(str2+'\n')
                t +=1
            find_ix +=1
            last_str=this_str
        else:
            sold_list.append('*'+a1)
f.close()
