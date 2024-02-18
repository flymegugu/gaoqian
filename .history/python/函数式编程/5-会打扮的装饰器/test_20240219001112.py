"""
Date: 2024-02-19 00:09:12
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-19 00:09:17
FilePath: /tools/python/函数式编程/5-会打扮的装饰器/test.py
Description: 
"""
from typing import Any


class CallableObject:
    def __call__(self, *args, **kwargs):
        print('调用对象',args,kwargs)

callable_obj=CallableObject()

ca