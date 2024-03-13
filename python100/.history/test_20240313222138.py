"""
Date: 2024-02-07 18:32:24
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-03-13 21:46:46
FilePath: /python100/test.py
Description: 
"""
def check_num(digit):
    count = 0 
    with open('xxx.txt','r') as f:
        for i in f:
            for l in i:
                if l.isdigit():
                    count+=1
        return count

    print(count)
    f.close()
