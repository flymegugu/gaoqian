'''
Date: 2024-02-20 23:20:21
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-20 23:24:38
FilePath: /python/类/3-类方和静态方法/类方法.py
Description: 类实例化dui 
'''

class A(object):
    bar=1
    @classmethod
    def class_foo(cls):
        print('hello',cls)
        print(cls.bar)
print(A.class_foo())