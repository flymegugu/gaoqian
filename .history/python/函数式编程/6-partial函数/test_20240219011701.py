"""
Date: 2024-02-19 01:12:01
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-19 01:12:04
FilePath: /tools/python/函数式编程/6-partial函数/test.py
Description: partial 接收函数 test 作为参数，固定 test 的参数 y=3，并返回一个新的函数给 test
"""

from functools import partial


def test(x, y):
    return x - y


f = partial(test, 3)
print(f(10)) #此处的10会传递给y
