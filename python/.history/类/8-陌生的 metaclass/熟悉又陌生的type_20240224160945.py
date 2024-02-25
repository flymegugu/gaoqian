"""
Date: 2024-02-24 16:01:25
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-24 16:01:27
FilePath: /python/类/8-陌生的 metaclass/熟悉又陌生的type.py
Description: 
"""


class Foo(object):
    pass


Foo = type("Foo", (object,), {})
print(Foo)
print(Foo())

class Foo(object):
    foo=True
    