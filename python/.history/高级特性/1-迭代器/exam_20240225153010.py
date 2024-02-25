'''
Date: 2024-02-24 16:17:08
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-25 15:29:25
FilePath: /python/高级特性/1-迭代器/exam.py
Description: 
'''
from collections import Iterable

print(isinstance((),Iterable))
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance(100,Iterable))


for x in [1,2,3]:
    print(x)
it=iter([1,2,3,4])
while True:
    try:
        x=next(it)
        print(x) 
    except StopIteration:
        break