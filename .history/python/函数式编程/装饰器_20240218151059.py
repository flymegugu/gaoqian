"""
Date: 2024-02-18 01:25:44
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-18 15:08:49
FilePath: /tools/python/函数式编程/装饰器.py
Description: 
"""

"""
Date: 2024-02-18 01:25:44
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-18 12:58:03
FilePath: /tools/python/装饰器.py
LastEditTime: 2024-02-18 10:38:42
FilePath: /tools/python/装饰器.py
Description: 
    函数可以被赋值给其他变量
    函数可以被删除
    可以在函数里面再定义函数
    函数可以作为参数传递给另外一个函数
    函数可以作为另一个函数的返回

    装饰器可以定义多个，离函数定义最近的装饰器先被调用，比如：

@decorator_one
@decorator_two
def func():
    pass

等价于：

def func():
    pass

func = decorator_one(decorator_two(func))


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

############
# def makeitalic(func):
#     def wrapped():
#         return "<i>" + func() + "</i>"

#     return wrapped

# @makeitalic
# def hello():
#     return "hello world"


# print(hello())
####带参数装饰器
def makeitalic(func):
    def wrapped(*args, **kwargs):
        ret = func(*args, **kwargs)
        return "<i>" + ret + "<\i>"

    return wrapped


@makeitalic
def hello(name):
    return "hello %s" % name"


@makeitalic
def hello2(name1, name2):
    return "hello %s,%s" % (name1, name2)

hello()
hello2()