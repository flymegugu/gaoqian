"""
Date: 2024-02-16 18:15:02
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-16 18:15:07
FilePath: /tools/python/匿名函数.py
Description: 
"""


def func(func1, arr):
    return [func1(x) for x in arr]



arr = func(add_one,[1,2,3,4])
print(arr)