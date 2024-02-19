"""
Date: 2024-02-19 22:52:58
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-19 22:53:01
FilePath: /tools/python/类/1-类和实例/访问限制.py
Description: 
"""
class Animal(object):
    def __init__(self,name):
        self.__name=name

    def greet(self):
        print('hello,i am %s'% self.__name)
test = Animal(''