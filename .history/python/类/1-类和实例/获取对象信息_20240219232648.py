"""
Date: 2024-02-19 23:02:29
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-19 23:02:34
FilePath: /tools/python/类/1-类和实例/获取对象信息.py
Description: 
"""
class Animal(object):
    def __init__(self,name):
        self.name=name
    def greet(self):
        print('hello iam %s'% self.name)

dog1=Animal('dog1')
dog1.greet()
print(type(dog1))
print(isinstance(dog1,Animal))
print(getattr(dog1,'name'))