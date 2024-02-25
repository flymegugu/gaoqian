"""
Date: 2024-02-24 16:01:25
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-24 16:01:27
FilePath: /python/类/8-陌生的 metaclass/熟悉又陌生的type.py
Description: 
"""


class Foo(object):
    Foo = True
print(type(Foo))
print(type(Foo()))


class Base(object):
    pass

class Foo(object):
    foo=True

type('Foo',(Base, ),{'foo'})