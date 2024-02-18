"""
Date: 2024-02-18 01:25:44
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-18 10:38:42
FilePath: /tools/python/装饰器.py
Description: 
"""


def hello():
    return "hello world"


def zhuangshi(func):
    def wrapped():
        return "didididi" + func() + "didididi"

    return wrapped


a = zhuangshi(hello)
