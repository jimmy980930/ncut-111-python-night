# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:18:51 2022

@author: jimmy
"""

#built-ins內建函式
#global 全域
#enclosing封閉
#local區域

a=b=c=1

def test(b):
    global c
    c=9
    a=22
    print('區域a,b全域c',a,b,c)
    
test(3)
print(a,b,c)