'''
Date: 2024-01-14 17:54:03
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-01-20 15:59:32
FilePath: /tools/python100/14.py
Description: 
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
'''
import string
test = input("请输入字符串:\n")
letters = 0 
space = 0
digit = 0 
others = 0 
for c in test:
    if c.isalpha():
        letters += 1
    elif c.isspace():
       space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print('char = %d,space = %d,digit = %d,others = %d'% (letters,space,digit,others))