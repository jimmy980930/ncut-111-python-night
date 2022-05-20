# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 18:34:18 2022

@author: user
"""

a=['a.txt','b.txt','c.txt']

c=','.join(a)

b=c.replace('txt','bmp').split(',')

print(b)