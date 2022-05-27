# -*- coding: utf-8 -*-
"""
Created on Fri May 27 18:27:50 2022

@author: jimmy
"""

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
'''

def prn(name, **key):
    print(f'{name},',key )

prn('不定位置變數打包= -> :',red=1, blue=2, yellow=3)

dict1={'white':4, 'black':5, 'gray':6}
prn('不定數量指定參數 dict輸入', **dict1) # **為字典必要, *為字串list