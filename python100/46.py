"""
Date: 2024-02-11 11:38:29
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-02-11 11:44:36
FilePath: /tools/python100/46.py
求输入数字的平方，如果平方运算后小于 50 则退出。
"""

TURE=1
FALSE=0
def SQ(x):
    return x * x 
print("如果平方数小于 50，那么就退出程序")
again= 1
while again:
    a = int(input('请输入：'))
    print("输入的值为%d" % (SQ(a)))
    if SQ(a) >= 50:
        again = TURE
    else:
        again = FALSE
