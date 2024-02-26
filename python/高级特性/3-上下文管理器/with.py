"""
Date: 2024-02-26 11:38:48
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 11:38:52
FilePath: /python/高级特性/3-上下文管理器/with.py
Description:除了自定义上下文管理器，Python 中也提供了一些内置对象，可直接用于 with 语句中，比如最常见的文件操作。

传统的文件操作经常使用 try/finally 的方式，比如： 
"""

file = open("somefile", "r")
try:
    for line in file:
        print(line)
finally:
    file.close()
# 可以看到，通过使用 with，代码变得很简洁，而且即使处理过程发生异常，with 语句也会确保我们的文件被关闭。#
with open('somefile','r') as file:
    for line in file:
        print(line)
