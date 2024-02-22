"""
Date: 2024-02-22 10:18:29
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-22 10:18:32
FilePath: /python/类/4-定制类和魔法方法/iter.py
Description: 
"""
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
fib=Fib()
for i in fib:
    if i>10:
        break