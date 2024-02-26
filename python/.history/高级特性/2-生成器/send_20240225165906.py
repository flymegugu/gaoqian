"""
Date: 2024-02-25 16:28:16
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-25 16:54:26
FilePath: /python/高级特性/2-生成器/send.py
Description:可以看到，上面的函数没有使用 return 语句返回值，而是使用了 yield『生出』一个值。一个带有 yield 的函数就是一个生成器函数，当我们使用 yield 时，它帮我们自动创建了 __iter__() 和 next() 方法，而且在没有数据时，也会抛出 StopIteration 异常，也就是我们不费吹灰之力就获得了一个迭代器，非常简洁和高效。

带有 yield 的函数执行过程比较特别：

    调用该函数的时候不会立即执行代码，而是返回了一个生成器对象；
    当使用 next() (在 for 循环中会自动调用 next()) 作用于返回的生成器对象时，函数开始执行，在遇到 yield 的时候会『暂停』，并返回当前的迭代值；
    当再次使用 next() 的时候，函数会从原来『暂停』的地方继续执行，直到遇到 yield 语句，如果没有 yield 语句，则抛出异常；

整个过程看起来就是不断地 执行->中断->执行->中断 的过程。一开始，调用生成器函数的时候，函数不会立即执行，而是返回一个生成器对象；然后，当我们使用 next() 作用于它的时候，它开始执行，遇到 yield 语句的时候，执行被中断，并返回当前的迭代值，要注意的是，此刻会记住中断的位置和所有的变量值，也就是执行时的上下文环境被保留起来；当再次使用 next() 的时候，从原来中断的地方继续执行，直至遇到 yield，如果没有 yield，则抛出异常。

简而言之，就是 next 使函数执行，yield 使函数暂停。 
"""

def generator_function():
    value1 =yield 0
    print('value1 is ',value1)
    value2 =yield 1
    print('value1 is ',value2)
    value3 =yield 2 
    print('value1 is ',value3)

g=generator_function()
print(next(g))
print(next(g))
print(next(g))
# g.send(2)
# g.send(3)
# g.send(4)
