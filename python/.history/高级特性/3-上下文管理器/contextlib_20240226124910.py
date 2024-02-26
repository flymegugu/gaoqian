'''
Date: 2024-02-26 12:45:16
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 12:49:05
FilePath: /python/高级特性/3-上下文管理器/contextlib.py
Description: 
'''
from contextlib import contextmanager
@contextmanager
def point(x,y):
    print('before yield')
    yield x*x