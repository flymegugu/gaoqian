"""
Date: 2024-02-11 22:26:21
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2024-02-11 22:26:30
FilePath: /tools/python100/47.py
Description: 两个变量值互换
"""

if __name__ == "__main__":
    i = 10
    j = 20
    if i > j:
        print("%d 大于 %d" % (i, j))
    elif i == j:
        print("%d 等于 %d" % (i, j))
    elif i < j:
        print("%d 小于 %d" % (i, j))
    else:
        print("未知")
