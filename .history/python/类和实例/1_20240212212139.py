"""
Date: 2024-02-12 20:44:09
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-12 20:44:16
FilePath: /tools/python/类和实例/1.py
Description: 
"""


class animal(object):
    def __init__(self, name):
        self.__name = name

    def test(self):
        print("hello i am is %s" % (self.__name))


a = animal("tom")
print(type(a))
print(a.name)
a.test()
