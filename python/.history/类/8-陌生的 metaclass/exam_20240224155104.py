"""
Date: 2024-02-24 15:46:25
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-24 15:47:51
FilePath: /python/类/8-陌生的 metaclass/exam.py
Description: 
"""


class Foo(object):
    foo = True


class Bar(object):
    bar = True


def echo(cls):
    print(cls)


def select(name):
    if name == "foo":
        return Foo
    if name == "bar":
        return Bar
echo(Foo)