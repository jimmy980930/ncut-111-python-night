# -*- coding: utf-8 -*-
"""
Created on Fri May 20 18:46:48 2022

@author: user
"""
'''
def student(name, nick='開剁'):
    print(name ,nick)
    
student('阿巴阿巴')
'''
'''
def a(w,h):
    return w+h , w*h+1
b, c=a(3 ,5)
print(b , c)
'''

'''
def ab(w,h):
    return [(w+h , w*h+1), '正方形'if w==h else'長方形']
((b, c),d)=ab(5, 5)
print(b , c, d)
'''

'''
s=[(1,2),(3,4),(5,6),(7,8)]

def clac(w,h):
    return w*h

def clacAll(conta, func): #func=clac, s=conta
    for r in conta:
        print(func(r[0], r[1]), end=' ') #以元素的 寬W 高H 為參數呼叫
        
clacAll(s, clac)
'''
'''
def add(x):
    b=0
    for i in range(1,x):
        b+=1
        x+=b
    return x

def mul(x):
    b=0
    for i in range(1,x):
        b+=1
        x*=b
    return x

def clacAll(value, func):
    return func(value)

print(clacAll(10, add))
print(clacAll(10, mul))
'''
'''
def add(x):
    v=0
    for i in x:
        v+=i
    return v

def mul(x):
    v=1
    for i in x:
        v*=i
    return v

def clacAll(value, func):
    return func(value)

x=[1,2,4]
funcs=[add, mul]
for f in funcs:
    print(clacAll(x, f))
'''

def calc(w, *args): # (乘號) *name表不定數量的參數
    for arg in args:
        w= w* arg
    return w
y = calc(2 , 4,5,6,7) # 2以外都是args參數
print(y)

def prn( name ,**drink): # **name 不定數量的指定參數 ex: a=1 ,b=2 ==>drink
    print(name ,drink)
prn('查爾斯',a='手沖',b='暴沖')
    