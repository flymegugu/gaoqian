"""
Date: 2024-02-02 16:42:48
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-02-02 16:42:50
FilePath: /work_tools/Users/maxgu/Desktop/MaxGu/tools/python100/34.py
Description:使用函数，输出三次 RUNOOB 字符串。 
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-


def hello_runoob():
    print("RUNOOB")


def hello_runoobs():
    for i in range(3):
        hello_runoob()


if __name__ == "__main__":
    hello_runoobs()
