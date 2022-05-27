# -*- coding: utf-8 -*-
"""
Created on Fri May  6 19:17:32 2022

@author: user
"""

str='abcdefg'

str2=[ i for i in str]
print(str2)

str3={ i:1 for i in str }
print(str3)

str4=( j+3 for j in range(1,5))
print(tuple(str4))



'''
s=[ i*i for i in range(10) if i%2==0 ]
print(s)
'''
'''
a=[[1,2,3,4,5,6,7,8,9],[1,3,5,7,9],[2,4,6,8]]

b=[e2 for e1 in a for e2 in e1 if e2 != 4]

print(b)
'''