"""
Date: 2024-02-22 18:04:40
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-22 18:05:02
FilePath: /python/类/5-slots 魔法/example.py
Description: 
"""
class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
p =Point(3,4)
print(p)
print(p.x)
p.z=5
print(p.z)
print(p.__dict__)

#########
class Point(object):
    __slots__=('x','y')