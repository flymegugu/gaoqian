"""
Date: 2024-02-16 23:43:44
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-16 23:43:46
FilePath: /tools/python/闭包.py
Description: 
"""
from math import pow 
def make_pow(n):
    def inner_func(x):
        return  pow(x,n)
    return inner_func

pow2=make_pow(2)
print(pow2)
a =pow2(6)
print(a)