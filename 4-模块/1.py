'''
Date: 2024-01-07 15:58:46
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2024-01-09 22:38:55
FilePath: /tools/4-模块/1.py
Description: 随机数
'''
def spam(a1):
    try:
        return 42/a1
    except ZeroDivisionError:
        print('error invalid ar')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(10))