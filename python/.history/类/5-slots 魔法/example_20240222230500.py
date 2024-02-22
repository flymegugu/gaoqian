"""
Date: 2024-02-22 18:04:40
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-22 18:05:02
FilePath: /python/类/5-slots 魔法/example.py
Description: 使用 __slots__ 有一点需要注意的是，__slots__ 设置的属性仅对当前类有效，对继承的子类不起效，除非子类也定义了 __slots__，这样，子类允许定义的属性就是自身的 slots 加上父类的 slots。
"""

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p = Point(3, 4)
print(p)
print(p.x)
p.z = 5
print(p.z)
print(p.__dict__)


print("#########")

class Point(object):
    __slots__ = ("x", "y")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
p=Point(3,4)
p.z=44
print(p)
