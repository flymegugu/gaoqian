'''
Date: 2023-12-22 09:31:27
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2023-12-22 12:51:29
FilePath: /tools/2.py
'''

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和：%d"%(n,sum))