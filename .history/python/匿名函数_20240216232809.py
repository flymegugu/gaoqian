"""
Date: 2024-02-16 18:15:02
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-16 18:15:07
FilePath: /tools/python/匿名函数.py
Description: https://www.youtube.com/watch?v=bupBl442F9c
"""


def add_one(x):
    return x + 1


def func(func1, arr):
    return [func1(x) for x in arr]


arr = func(add_one, [1, 2, 3, 4])
print(arr)
#####以上内容等同于以下内容,可以通过 lambda 实现的需求，不用小题大做用 def
arr = func(lambda x: x + 1, [1, 2, 3, 4])
print(arr)
