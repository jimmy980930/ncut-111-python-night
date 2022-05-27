# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:10:30 2022

@author: jimmy
"""

#lambda x : 回傳值
'''
def lam(func,value):
    return func(value)

a = lambda x:list(range(1,x+1))

print(lam(a,5))
'''

#sorted touple排序

s = [(1,2),(3,4),(4,5),(1,5)]

result = sorted( s , key = lambda e:e[0])
result2 = sorted( s , key = lambda e:e[1])

print(result)
print(result2)

