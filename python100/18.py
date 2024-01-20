'''
Date: 2024-01-19 00:12:07
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-01-19 21:38:50
FilePath: /tools/python100/18.py
Description: 
'''
from functools import reduce
tn = 0
sn = []
n = int(input('n='))
a = int(input('a='))
for count in range(n):
    tn = tn + a
    a = a * 10