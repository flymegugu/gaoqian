"""
Date: 2024-02-25 15:45:09
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-25 15:56:39
FilePath: /python/高级特性/2-生成器/exam.py
Description:就是 next 使函数执行，yield 使函数暂停。
 
"""

numbers = (x for x in range(5))
for n in numbers:
    print(n)


def generator_func():
    print('hello 1')
    yield 1
    print('hello 2')
    yield 2
    print('hello 3')
g=generator_func()
print(g)
print(next(g))
print(next(g))
print(next(g))

def fib():
    a,b=0,1
    while True:
        a,b=b,a+b
    yield a
f= fib()
for 