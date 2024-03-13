"""
Date: 2024-02-07 18:32:24
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-03-13 21:46:46
FilePath: /python100/test.py
Description: 
"""
k=[]
with open('xxx.txt','r') as f:
    for i in f:
        print(i) 
        for l in i:
            if l.isdigit():
                print(l)
                k.append

    f.close()
