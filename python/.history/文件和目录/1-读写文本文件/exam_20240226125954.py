'''
Date: 2024-02-26 12:54:23
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 12:59:43
FilePath: /python/文件和目录/1-读写文本文件/exam.py
Description: 
'''
with open("文件和目录/data.txt", "r") as f:
    lines=f.readlines()
    # print(lines)
    line_num=len(lines)
    print(line_num)