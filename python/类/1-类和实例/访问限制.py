"""
Date: 2024-02-19 22:52:58
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-19 22:53:01
FilePath: /tools/python/类/1-类和实例/访问限制.py
Description: 需要注意的是，在 Python 中，以双下划线开头，并且以双下划线结尾（即 __xxx__）的变量是特殊变量，特殊变量是可以直接访问的。所以，不要用 __name__ 这样的变量名。

另外，如果变量名前面只有一个下划线 _，表示不要随意访问这个变量，虽然它可以直接被访问。
"""

class Animal(object):
    def __init__(self,name):
        self.__name=name

    def greet(self):
        print('hello,i am %s'% self.__name)
test = Animal('tom')
# test.__name #私有属性不被允许使用
test.greet()#但是可以通过类的函数进行引用私有属性
