'''
Date: 2024-01-09 22:44:42
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2024-01-09 22:44:46
FilePath: /tools/5-异常/1.py
Description: 
'''
def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
