"""
Date: 2024-02-13 15:11:02
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-14 02:18:31
FilePath: /tools/python/高阶函数.py
Description: 
"""

# def func(g, arr):
#     return [g(x) for x in arr]


# def double(x):
#     return 2 * x


# def square(x):
#     return x * x
# arr1=func(double,[1,2,3,4])
# arr2=func(square,[1,2,3,4])


# print(arr1)
# print(arr2)
####
def double(x):
    return 2 * x


def triple(x):
    return 3 * x


def square(x):
    return x * x
funcs=[double,triple,square]
value=list(map(lambda f:f(4),funcs))