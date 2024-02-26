"""
Date: 2024-02-26 12:54:23
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 13:34:18
FilePath: /python/文件和目录/1-读写文本文件/字节.py
Description:我们使用 f.read(1024) 来每次读取 1024 个字节（1KB） 的文件内容，将其存到 piece，再对 piece 进行处理。 
"""

with open("文件和目录/data.txt", "r") as f:
    while True:
        piece=f.read(1024)
        if not piece:
            break
        print(piece)
def read_in_chunk(file_object,chunk_size=1024):
    while True:
        data=file_object.read(chunk_size)
        if not data:
            break
        yield data

with open("文件和目录/data.txt", "r") as f:
    for piece in read_in_chunk(f):