"""
Date: 2024-02-23 11:33:48
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-23 11:33:51
FilePath: /python/类/4-定制类和魔法方法/super.py
Description: 
"""
class Animal(object):
    def __init__(self,name):
        self.name=name
    def greet(self):
        print('hello %s'% self.name)
class Dog(Animal):
    def greet(self):
        super().greet()
        print("wwwwww")
