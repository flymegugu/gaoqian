"""
Date: 2024-02-19 23:56:49
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-19 23:56:51
FilePath: /tools/python/类/1-类和实例/继承和多态.py
Description: 
"""


class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("hello iam %s" % self.name)


class dog(Animal):
    def greet(self):
        print("wangwang i am %s" % self.name)
    def run(self):
        print('i am running')


test = dog("kkkk")
test.greet()
test.run()
##

class Animal(object):
    def __init__(self,name):
        self.name=name

    def greet(self):
        p