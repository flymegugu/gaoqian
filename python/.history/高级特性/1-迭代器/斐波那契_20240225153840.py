"""
Date: 2024-02-25 15:32:47
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-25 15:36:54
FilePath: /python/高级特性/1-迭代器/斐波那契.py
Description: 
"""


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
def main():
    fib=Fib()
    print('isinstance(fib,Iterator):',isinstance(fib,Iterator))