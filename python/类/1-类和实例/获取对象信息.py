"""
Date: 2024-02-19 23:02:29
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-19 23:02:34
FilePath: /tools/python/类/1-类和实例/获取对象信息.py
Description: 
    类是具有相同属性和方法的一组对象的集合，实例是一个个具体的对象。
    方法是与实例绑定的函数。
    获取对象信息可使用下面方法：
        type(obj)：来获取对象的相应类型；
        isinstance(obj, type)：判断对象是否为指定的 type 类型的实例；
        hasattr(obj, attr)：判断对象是否具有指定属性/方法；
        getattr(obj, attr[, default]) 获取属性/方法的值, 要是没有对应的属性则返回 default 值（前提是设置了 default），否则会抛出 AttributeError 异常；
        setattr(obj, attr, value)：设定该属性/方法的值，类似于 obj.attr=value；
        dir(obj)：可以获取相应对象的所有属性和方法名的列表：

"""

class Animal(object):
    def __init__(self,name):
        self.name=name
    def greet(self):
        print('hello iam %s'% self.name)

dog1=Animal('dog1')
dog1.greet()
print(type(dog1))
print(isinstance(dog1,Animal))
print(getattr(dog1,'name'))
print(dir(dog1))
