"""
Date: 2024-02-28 23:58:02
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-28 23:59:08
FilePath: /python/函数使用/partial.py
Description: 
"""

from functools import partial


def add_num(a, b, c,d):
    return a + b + c+d


sum_numbers = partial(add_num, 10, 20)
result = sum_numbers(30,33)
print(result)
