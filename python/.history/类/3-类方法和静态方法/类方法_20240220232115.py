'''
Date: 2024-02-20 23:20:21
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-20 23:20:24
FilePath: /python/类/3-类方法和静态方法/类方法.py
Description: 
'''

class A(object):
    bar=1
    @classmethod
    def class_foo(cls):
        print('hello',cls)
        print(cls.bar)
