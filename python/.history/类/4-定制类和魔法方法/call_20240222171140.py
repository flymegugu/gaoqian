"""
Date: 2024-02-22 17:10:18
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-22 17:10:21
FilePath: /python/类/4-定制类和魔法方法/call.py
Description: 
"""

from typing import Any


class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __call__(self, z):
        return self.x + self.y + z
p = Point(3,4)


