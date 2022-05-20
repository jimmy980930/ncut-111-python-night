# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 20:18:40 2022

@author: user
"""
'''
for a in range(1,10):
    for b in range(1,10):
        print(b,'*',a,'=',a*b,end=' ')
        if b==9:
            print(end=' \n')
a+=a
'''

'''

a=0
c=1

for b in range(1,82):
    a=a+1
    
    print(a,'*',c,'=',a*c,end='\t')
    
    if a%9==0:
        c+=1
        a=0
        print('\n')

'''



j=[[1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]

k=0

l=0

for i in range(1,82):
    if k>8:
       k=0
       l=l+1
       print('\n')
k=k+1
print(j[l][k],'*',k,'=',j[l][k]*k)


        

    

