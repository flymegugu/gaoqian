"""
Date: 2024-02-19 23:56:49
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-19 23:56:51
FilePath: /tools/python/类/1-类和实例/继承和多态.py
Description:
    继承可以拿到父类的所有数据和方法，子类可以重写父类的方法，也可以新增自己特有的方法。
    有了继承，才有了多态，不同类的对象对同一消息会作出不同的相应。
 
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
        print("i am running")


test = dog("kkkk")
test.greet()
test.run()
##


class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("ddddd%s" % self.name)


class Dog(Animal):
    def greet(self):
        print("dddd%s" % self.name)


class Cat(Animal):
    def greet(self):
        print("ssss%s" % self.name)

a =Dog('dddd')
a.greet()


a =Cat('dddd')
a.greet()
