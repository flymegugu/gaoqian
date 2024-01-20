'''
Date: 2024-01-20 17:33:08
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-01-20 18:17:15
FilePath: /tools/python100/20.py
Description:题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？ 
'''

tour = []
height = []
hei = 100.0
tim = 10

for i in range(1,tim + 1):
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2*hei)
    hei /= 2
    #height存放的是反弹的高度
    height.append(hei)
print('总高度：tour={0}'.format(sum(tour)))
print('第十次反弹高度:height={0}'.format(height[-1]))