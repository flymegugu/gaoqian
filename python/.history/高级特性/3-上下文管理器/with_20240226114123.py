"""
Date: 2024-02-26 11:38:48
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 11:38:52
FilePath: /python/高级特性/3-上下文管理器/with.py
Description: 
"""

file = open("somefile", "r")
try:
    for line in file:
        print(line)
finally:
    file.close(）
