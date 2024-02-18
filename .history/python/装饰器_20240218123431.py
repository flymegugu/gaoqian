"""
Date: 2024-02-18 01:25:44
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-18 10:38:42
FilePath: /tools/python/装饰器.py
Description: 
    函数可以被赋值给其他变量
    函数可以被删除
    可以在函数里面再定义函数
    函数可以作为参数传递给另外一个函数
    函数可以作为另一个函数的返回

"""

# def hello():
#     return "hello world"


# def zhuangshi(func):
#     def wrapped():
#         return "didididi" + func() + "didididi"

#     return wrapped


# a = zhuangshi(hello)
# print(a())
# print(a.__name__)


def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"


def hello():
    return "hello world"


hello1 = makeitalic(hello)
hello1()