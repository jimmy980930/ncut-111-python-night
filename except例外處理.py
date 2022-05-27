# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:12:58 2022

@author: user
"""

'''
str=input('please enter a number=')

try:
    number = int(str)
    print(you'r input is =',number)



except BaseException as e:
    print('error! ')
    print(e)

expect Excpetion as e:

expect ValueError as e:
    
expect UnicodeTranslateError as e:
'''

while True:
    s=input('請輸入100的除數')
    try:
        i = 100 / float(s)
        print('100除', s , '=' , i)
        break
    
    except ValueError as e:
        print('發生 valueError 例外:' , e)
    except ZeroDivisionError:
        print('發生 ZeroDivisionError 例外:')
    except :
        print('其他例外')
        
    print('進入下一個迴圈')
    
    
print('程式正常結束')