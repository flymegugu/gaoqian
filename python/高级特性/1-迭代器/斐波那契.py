"""
Date: 2024-02-25 15:32:47
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-25 15:36:54
FilePath: /python/高级特性/1-迭代器/斐波那契.py
Description:
    元组、列表、字典和字符串对象是可迭代的，但不是迭代器，不过我们可以通过 iter() 函数获得一个迭代器对象；
    Python 的 for 循环实质上是先通过内置函数 iter() 获得一个迭代器，然后再不断调用 next() 函数实现的；
    自定义迭代器需要实现对象的 __iter()__ 和 next() 方法（注意：Python3 要实现 __next__() 方法），其中，__iter()__ 方法返回迭代器对象本身，next() 方法返回容器的下一个元素，在没有后续元素时抛出 StopIteration 异常。
 
"""

from collections import Iterator

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


def main():
    fib = Fib()
    print("isinstance(fib,Iterator):", isinstance(fib, Iterator))
    for i in fib:
        if i > 10:
            break
        print(i)


if __name__ == "__main__":
    main()
