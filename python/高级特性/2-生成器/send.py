"""
Date: 2024-02-25 16:28:16
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-25 16:54:26
FilePath: /python/高级特性/2-生成器/send.py
Description:使用生成器的方法非常简洁，不用自定义 __iter__() 和 next() 方法。
    yield 把函数变成了一个生成器。
    生成器函数的执行过程看起来就是不断地 执行->中断->执行->中断 的过程。
        一开始，调用生成器函数的时候，函数不会立即执行，而是返回一个生成器对象；
        然后，当我们使用 next() 作用于它的时候，它开始执行，遇到 yield 语句的时候，执行被中断，并返回当前的迭代值，要注意的是，此刻会记住中断的位置和所有的数据，也就是执行时的上下文环境被保留起来；
        当再次使用 next() 的时候，从原来中断的地方继续执行，直至遇到 yield，如果没有 yield，则抛出异常。
 
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
