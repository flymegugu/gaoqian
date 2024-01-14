'''
Date: 2024-01-14 16:59:14
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-01-14 17:11:02
FilePath: /tools/python100/12.py
Description: 
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from math import sqrt

# 创建一个空列表来存储素数
prime_numbers = []

# 从101到200遍历每个数字
for i in range(101, 201):
    # 初始化变量succ为1，表示当前数字为素数
    succ = 1
    
    # 计算当前数字的平方根，并将其转换为整数
    k = int(sqrt(i + 1))
    
    # 从2到k遍历每个数字
    for j in range(2, k + 1):
        # 如果当前数字可以被当前遍历的数字整除，则将succ设置为0，并跳出当前循环
        if i % j == 0:
            succ = 0
            break
    
    # 如果succ仍然为1，表示当前数字为素数，将其添加到列表中
    if succ == 1:
        prime_numbers.append(i)

# 打印素数列表和素数的数量
print("素数列表:", prime_numbers)
print("素数的数量:", len(prime_numbers))