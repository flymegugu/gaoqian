'''
Date: 2023-12-23 19:26:42
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2023-12-23 19:28:56
FilePath: /tools/1-循环/8.py
Description: 
'''
for letter in 'runood':
    if letter == 'o':
        continue
    print(letter)
var = 10 
while var > 0:
    var -= 1
    if var == 5:
        continue
    print(var)
print("good bye")

