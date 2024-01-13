'''
Date: 2024-01-13 16:16:29
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2024-01-13 16:46:36
FilePath: /tools/python100/6.py
Description:斐波那契 
'''
def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
        print(a)
        
print(fib(10))