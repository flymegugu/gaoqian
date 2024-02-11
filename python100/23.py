'''
Date: 2024-01-22 12:42:11
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2024-01-22 12:57:35
FilePath: /tools/python100/23.py
   *
  ***
 *****
*******
 *****
  ***
   *

'''
from sys import stdout
for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print('')
 
for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print('')