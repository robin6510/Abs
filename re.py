# -*- coding: GBK -*-

import sys,string,time,re

#get parameters
f=open('w064_result.txt')
str1=f.read()
str2=re.findall(r"\--+(.+?)\+F3=Exit",str1)
print len(str2)
str3=str2[0]
print str3
sys.exit(1)
str3=str2[0]

#获取结果部分
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

# 获取参数部分, 包括sold# ,两个date, product
op_check=str1.replace(str3,'')
check_list=[]
#获取sold# 的语句
str2=re.findall(r'Sold#\d{7}',op_check)
str5=str2[0]
check_list.append(str5.replace('Sold#',''))
#获取date的语句
str2=re.findall(r'Start Ship Date From [\d\/+]{6,8}To [\d\/+]{6,8}',op_check)
str5=str2[0].replace('Start Ship Date From','')
str5=str5.replace('To','').replace('/','').replace(' ','0')
check_list.append(str5[0:6])
check_list.append(str5[6:12])
#获取product 的语句
str2=re.findall(r'Product....:.{1,4}Only Div',op_check)
str5=str2[0].replace('Product....:','').replace('Only Div','').replace(' ','')
check_list.append(str5)
#print "{:0>7d}".format(int(check_list[0]))
# sold :    Sold#\d{7}
# date :    Start Ship Date From [\d\/+]{6,8}To [\d\/+]{6,8}
#product :  Product....:.{1,4}Only Div
#   [A-Z\>][a-zA-Z\s\(]{1,30}\s[\d]{1,9}
