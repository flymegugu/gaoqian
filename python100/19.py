'''
Date: 2024-01-20 13:17:17
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-01-20 15:46:44
FilePath: /tools/python100/19.py
Description:题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。 
'''
from sys import stdout
for i in range(2,1002):
    list = []
    count = -1
    num = i
    for j in range(1,i):
        if i % j == 0:
            count += 1
            num -= j
            list.append(j)

    if num == 0:
        print(i)
        for j in range(count):
            stdout.write(str(list[j]))
            stdout.write(' ')
        print (list[count])