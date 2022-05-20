# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 20:14:35 2022

@author: user
"""

'''
右邊視窗varisble explorer
行數 數字的紅點為停頓點
'''

q=[[1,2,3,4],[5,4,5,3,1],[8,5,6,3,]]

count=0

for w in q:
    for e in w:
        if e==3:
            count+=1
print('共',count,'個3')