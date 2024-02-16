"""
Date: 2024-02-13 11:39:42
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-13 11:40:04
FilePath: /tools/python/可变参数.py
Description: 
"""


def add(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("numbers:", numbers)
    return sum


print(add())
print(add(1))
print(add(1, 2, 3))
###############
a = [1, 2]
print(add(*a))


# 关键字参数
def add(**kwargs):
    return kwargs


print(add())
print(add(x=2))

#############关键字参数
def sum(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        print(k)
        print(v)
        sum += v
    return sum
print(sum())
dict1={'x':23,'y':333}
print(sum(**dict1))
####组合参数
def func()