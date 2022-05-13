# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:04:49 2022

@author: user
"""
'''
def say(s=1):
    
    for a in range(s):
        print('never gona give you up')
        if s>=2:
            print('never gona let you down')
            
    print('==========')
    
say(10)

'''

'''
def add_and_sub(x,y):
    return x+y, x-y

z1, z2 =add_and_sub(1, 2)

print(z1)

print(z2)
'''
'''
def add(x):
    b=0
    for i in range(1,x):
        b+=1
        x+=b
    return x

z= add(10)
print(z)
'''

def add(x):
    b=0
    for i in range(1,x):
        b+=1
        x*=b
    return x

z= add(10)
print(z)