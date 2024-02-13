"""
Date: 2024-02-13 11:39:42
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-13 11:40:04
FilePath: /tools/python/可变参数.py
Description: 
"""
def add(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print('numbers:',numbers)
    return sum

print(add())
print(add(1))
print(add(1,2,3))
###############
a=[1,2]
print(add(*a)