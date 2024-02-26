'''
Date: 2024-02-26 13:44:18
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 13:44:21
FilePath: /python/文件和目录/1-读写文本文件/逐行读取.py
Description: 
'''

with open("文件和目录/data.txt", "r") as f:
    while True:
        line=f