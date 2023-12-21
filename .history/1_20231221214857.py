'''
Author: MaxGu flyme007@yeah.net
Date: 2023-12-21 16:39:27
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2023-12-21 21:48:32
FilePath: /tools/1.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%ran
'''
for num in range(0,20):
    for i in  range(2,num):
        if num%i == 0:
            j= num/i
            print('%d 等于 %d * %d'%(num,i,j))
            break
    
            