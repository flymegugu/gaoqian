"""
Date: 2024-02-13 15:11:02
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-14 22:16:23
FilePath: /tools/python/高阶函数.py
Description: 
"""

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
# def double(x):
#     return 2 * x


# def triple(x):
#     return 3 * x


# def square(x):
#     return x * x


# funcs = [double, triple, square]
# value = list(map(lambda t: t(4), funcs))
# print(value)

# test = lambda x: x + 5
# print(test(4))
# t1 = lambda a,b:a+b
# print(t1(2,3))

# numbers = [1, 2, 3, 4, 5]
# square_numbers = map(lambda x: x**2, numbers)
# for i in square_numbers:
#     print(i)

from functools import reduce
numbers = [1,2,3,4,5]
reduce(lambda x,y:x*y,numbers)