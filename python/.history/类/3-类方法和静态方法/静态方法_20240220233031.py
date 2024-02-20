"""
Date: 2024-02-20 23:28:28
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-20 23:29:30
FilePath: /python/类/3-类方法和静态方法/静态方法.py
Description: 在类中往往有一些方法跟类有关系，但是又不会改变类和实例状态的方法，这种方法是静态方法，我们使用 staticmethod 来装饰，比如下面的例子：
"""

class A(object):
    bar=1
    @staticmethod
    def static_foo():
        print('hello',A.bar)
a=A()
a.static_foo()
