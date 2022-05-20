# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

for a in 'abc':
    print(a, end=' ')
print('in str')
    
for b in {0,1,2}:
    print(b, end=' ')
print('in set')

for c in {'x':1,'Y':2,'Z':3}:
    print(c, end=' ')
print('in dict')

d={'j':1,'k':2,'l':3}
for key ,value in d.items():
    print(key,value)

for i in range(10):
    print(i,end=' ')
if i==9:
    print('\n')

'''
for o in range(0,10,2):
    print(o,end=' ')
'''

q=[[1,2,3,4],[5,4,5,3,1],[8,5,6,3,]]

count=0

for w in q:
    for e in w:
        if e==3:
            count+=1
print('共',count,'個3')