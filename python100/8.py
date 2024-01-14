'''
Date: 2024-01-13 20:55:56
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2024-01-13 21:04:13
FilePath: /tools/python100/8.py
Description: 99乘法表 
'''
for i in range(1,10):
    print(i)
    print()
    for j in range(1,1+i):
        print(j)
        print('%d * %d = %d'%(i,j,i*j),end=' ')
