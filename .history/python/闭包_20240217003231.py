"""
Date: 2024-02-16 23:43:44
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-16 23:43:46
FilePath: /tools/python/闭包.py
Description: 
"""
from math import pow 
def test(n):
    def inner_func(x):
        return pow(x,n)
    return inner_func

a = test(2)
print(a)
b=a(5)
print(