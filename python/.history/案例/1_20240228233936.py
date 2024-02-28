"""
Date: 2024-02-28 23:30:42
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-28 23:30:45
FilePath: /python/案例/1.py
Description: 
"""


def count_digits(fname):
    count = 0
    with open(fname) as file:
        for line in file:
            for i in line:
                if i.isdigit():
                    count += 1
        return count


a=count_digits("高级特性/3-上下文管理器/上下文管理器.py")
print(a)

def count_digit(fname):
    count=0
    block_size=1024 * 8
    with open(fname) as file:
        chunk=file.chunk(block_size)
        if not chunk:
            break
        for s in chunk:
            if s.isdigit():
                count+=1
    return count

