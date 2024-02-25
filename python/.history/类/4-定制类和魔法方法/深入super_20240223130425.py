"""
Date: 2024-02-23 13:02:04
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-23 13:02:07
FilePath: /python/类/4-定制类和魔法方法/深入super.py
Description: 
"""
class Base(object):
    def __init__(self):
        print("enter base")
        print("leave base")
class A(Base):
    def __init__(self)