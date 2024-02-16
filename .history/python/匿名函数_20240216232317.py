"""
Date: 2024-02-16 18:15:02
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-16 18:15:07
FilePath: /tools/python/匿名函数.py
Description: 
"""

def func(g,arr):
    return [g(x) for x in arr]

def add_one()