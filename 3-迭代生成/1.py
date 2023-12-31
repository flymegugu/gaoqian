'''
Date: 2023-12-25 15:29:42
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2023-12-27 13:22:53
FilePath: /tools/3-迭代生成/1.py
Description: 
'''
"""
Date: 2023-12-25 15:29:42
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2023-12-27 13:14:08
FilePath: /tools/3-迭代生成/1.py
Description: 
"""
import sys

list = [1, 2, 3, 4]
it = iter(list)
print(it)
print(it)
# for i in iter(list):
#     print(i,end='')

while True:
    try:
        print(next(it))
    except StopIteration:
        print("error")
        sys.exit()
