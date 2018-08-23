# -*- coding: GBK -*-

import sys,string,time,re



#get parameters

#re_op=re.compile(r'[A-Z\>][a-zA-Z\s\(]{1,30}\s[\d]{1,9}')


f=open('w064_result.txt')
str1=f.read()
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

d=dict(zip(new_list,list2))


print new_list
print list2
print d
                      
                      


#   [A-Z\>][a-zA-Z\s\(]{1,30}\s[\d]{1,9}
