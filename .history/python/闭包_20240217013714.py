"""
Date: 2024-02-16 23:43:44
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-16 23:43:46
FilePath: /tools/python/闭包.py
Description: 
"""

# from math import pow


# def test(n):
#     def inner_func(x):
#         return pow(x, n)

#     return inner_func


# a = test(2)
# b = a(5)
# print(b)

# print(b)
# test(3)
from math import sqrt
class Point(object):
    def __init__(self,x,y):
        self.x,self.y=x,y
    def get_distance(self,u,v):
        distance = sqrt((self.x-))