"""
Date: 2024-02-28 23:30:42
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-28 23:30:45
FilePath: /python/案例/1.py
Description: 
"""
def count_digits(fname):
    count =0
    with open(fname) as file:
        for line in file:
            for i in line:
                if i.isdigit():
                    count+=1
        retr