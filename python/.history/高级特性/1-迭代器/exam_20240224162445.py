'''
Date: 2024-02-24 16:17:08
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-24 16:24:27
FilePath: /python/高级特性/1-迭代器/exam.py
Description: 
'''
from collections import Iterable

print(isinstance((),Iterable))
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('str',Iterable))
print(isinstance(100,Iterable))