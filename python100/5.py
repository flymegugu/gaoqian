'''
Date: 2024-01-12 21:35:12
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2024-01-12 22:07:25
FilePath: /tools/python100/5.py
Description: 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
'''
# l = []
# for i in range(3):
    # x = int(input('请输入数字:'))
    # l.append(x)
# print(l)
l=[21,32,122]
a = l.sort()
print(a)
print(l)
b = sorted(l)
print(b)