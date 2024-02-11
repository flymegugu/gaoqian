"""
Date: 2024-01-27 15:21:22
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-01-27 15:21:26
FilePath: /tools/python100/27.py
Description: 
"""
def output(s,l):
    if l == 0:
        return
    print(s[l-1])
    output(s,l-1)
s = input('input a string:')
l = len(s)
output(s,l)