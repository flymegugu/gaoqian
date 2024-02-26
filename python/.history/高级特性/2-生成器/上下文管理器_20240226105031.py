"""
Date: 2024-02-26 10:24:16
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 10:49:43
FilePath: /python/高级特性/2-生成器/上下文管理器.py
Description: 
"""

from math import sqrt, pow


class Point(object):
    def __init__(self, x, y):
        print("initaial x and y")
        self.x, self.y = x, y

    def __enter__(self):
        print("entering context")
        return self

    def __exit__(self, type, value, traceback):
        print("exiting context")

    def get_distance(self):
        distance = sqrt(pow(self.x, 2) + pow(self.y, 2))
        return distance


with point(3, 4) as pt:
    print("distance:", pt.get_distance())
