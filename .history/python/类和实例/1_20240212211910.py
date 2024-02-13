"""
Date: 2024-02-12 20:44:09
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-12 20:44:16
FilePath: /tools/python/类和实例/1.py
Description: 
"""


class animal(object):
    def __init__(self, name):
        self.nhame = name

    def test(self):
        print("hello i am is %s" % (self.name))


a = animal("tom")
print(a.name)
a.test()
