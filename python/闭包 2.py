"""
Date: 2024-02-17 00:00:47
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-02-17 16:43:43
FilePath: /tools/python/1.py


    闭包是携带自由变量的函数，即使创建闭包的外部函数的生命周期结束了，闭包所引用的自由变量仍会存在。
    闭包在运行可以有多个实例。
    尽量不要在闭包中引用循环变量，或者后续会发生变化的变量。

"""

# def count():
#     funcs = []
#     for i in [1, 2, 3]:

#         def f():
#             return i


#     funcs.append(f)
#     return funcs
# count()
def count():
    funcs = []
    for i in [1, 2, 3]:

        def g(param):
            f = lambda: param
            return f

        funcs.append(g(i))
    return funcs


a = count()
print(a)
