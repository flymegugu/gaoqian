'''
Date: 2024-02-26 10:24:16
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 10:45:47
FilePath: /python/高级特性/2-生成器/上下文管理器.py
Description: 
'''

from math import sqrt,pow

class Point(object):
    def __init__(self,x,y):
        print('initaial x and y')
        self.x,self.y=x,y
    def __enter__