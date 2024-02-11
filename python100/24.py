'''
Date: 2024-01-22 21:01:03
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2024-01-22 21:18:35
FilePath: /tools/python100/24.py
Description: 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
程序分析：请抓住分子与分母的变化规律。 
'''
a = 2.0
b = 1.0
sum = 0.0
for i in range(0,20):
    sum += a / b
    print(a,b)
    a,b = a+b,a

print(" 和为%d"%sum)
    # num = a/b
    # print(num)
    # list.append(num)
    # print(list)