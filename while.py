# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 18:46:06 2022

@author: user
"""



'''WORK1->while():
n=float(input('請輸入一個實數:')) 

k=n

while(n>1):
    n=n-1
    k=k*n

print(k)
 '''

'''C&B
a=0
while(a<7):
    a+=1
    
    if a==5:
        continue
    print(f'a={a}')

b=10
while(b<20):
    b+=1
    
    if b==15:
        break
    print(f'b={b}')
print('跳出迴圈')
'''


while(1):
    a=input('請輸入通關密語:')
    
    if (a=='喵喵'):
        print('恭喜你過關了')
        break
     
    elif (a=='out'):
        break
    
print('再見!')  
        
        
        
