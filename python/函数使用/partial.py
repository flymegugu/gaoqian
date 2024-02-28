"""
Date: 2024-02-28 23:58:02
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-28 23:59:08
FilePath: /python/函数使用/partial.py
Description:partial 函数通常在以下情况下使用比较好：

固定函数的一部分参数：当你需要频繁调用一个函数，并且其中一部分参数是固定不变的，你可以使用 partial 函数来创建一个新的函数，该函数接受剩余的参数。这样可以减少代码的重复，提高代码的可读性和可维护性。
创建可组合的函数：partial 函数可以用于创建可组合的函数。你可以将多个 partial 函数组合在一起，形成一个新的函数，该函数接受所有的参数。这对于构建复杂的函数调用链非常有用。
调整函数的行为：通过使用 partial 函数，你可以在不修改原始函数的情况下，调整函数的行为。你可以固定部分参数，或者添加新的参数，以满足特定的需求。
实现函数的变体：如果你需要实现一个函数的多个变体，每个变体只在某些参数上有所不同，你可以使用 partial 函数来创建这些变体。这样可以避免重复编写相似的函数代码。

需要注意的是，使用 partial 函数创建的新函数是一个独立的函数对象，它与原始函数是分开的。因此，对新函数的调用不会影响原始函数的行为。另外，partial 函数通常用于在函数式编程和装饰器等场景中，以实现更灵活和可重用的代码。 
"""

from functools import partial


def add_num(a, b, c,d):
    return a + b + c+d


sum_numbers = partial(add_num, 10, 20)
result = sum_numbers(30,33)
print(result)
