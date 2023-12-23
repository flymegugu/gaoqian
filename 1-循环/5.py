'''
Date: 2023-12-23 18:58:13
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2023-12-23 19:15:40
FilePath: /tools/5.py
Description: range() 和 len() 函数以遍历一个序列的索引
'''
a = ['test','haha','hello','kk']
for i in range(len(a)):
    print(i,a[i])
    
print(list(range(5)))
