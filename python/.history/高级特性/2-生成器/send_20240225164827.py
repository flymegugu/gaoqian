'''
Date: 2024-02-25 16:28:16
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-25 16:48:27
FilePath: /python/高级特性/2-生成器/send.py
Description: 
'''

def generator_function():
    value1 =yield 0
    print('value1 is ',value1)
    value2 =yield 1
    print('value1 is ',value2)
    value3 =yield 2 
    print('value1 is ',value3)
    
g=generator_function()
print(next(g))
g.send(2)
g.send(3)
g.send(4)
