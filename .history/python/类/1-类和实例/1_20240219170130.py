"""
Date: 2024-02-19 16:46:27
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-19 16:46:30
FilePath: /tools/python/类/1-类和实例/1.py
Description: 
"""
class Animal(object):
    def __init__(self,name):
        self.name=name
    def greet(self):
        print('hello%s'%)