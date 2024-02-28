'''
Date: 2024-02-28 23:58:02
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-28 23:58:07
FilePath: /python/函数使用/partial.py
Description: 
'''

from functools import partial

def add_num(a,b,c):
    return a+b+c

sum_numbers=partial(add)