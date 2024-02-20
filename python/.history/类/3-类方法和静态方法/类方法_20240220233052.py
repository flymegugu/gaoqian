"""
Date: 2024-02-20 23:20:21
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-20 23:24:38
FilePath: /python/类/3-类方和静态方法/类方法.py
Description:在上面，我们使用了 classmethod 装饰方法 class_foo，它就变成了一个类方法，class_foo 的参数是 cls，代表类本身，当我们使用 A.class_foo() 时，cls 就会接收 A 作为参数。另外，被 classmethod 装饰的方法由于持有 cls 参数，因此我们可以在方法里面调用类的属性、方法，比如 cls.bar。 
"""

class A(object):
    bar=1
    @classmethod
    def class_foo(cls):
        print('hello',cls)
        print(cls.bar)
print(A.class_foo())
