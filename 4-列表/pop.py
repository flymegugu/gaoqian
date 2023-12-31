'''
Date: 2023-12-29 16:22:40
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2023-12-31 18:24:09
FilePath: /tools/4-列表/pop.py
Description:列表的添加和删除 
'''
motocycles = ['honda','yamaha','suzuki']
last_ownd = motocycles.pop()
print(f'最近一次购买的摩托车品牌是{last_ownd.title()}')
motocycles.remove('yamaha')
print(motocycles)
motocycles.insert(0,'test')
print(motocycles)
motocycles.sort()
print(motocycles)
motocycles.insert(2,'kkkkk1')
print(motocycles)
motocycles.sort(reverse=True)
print(motocycles)


cars = ['bmw','audi','toyota','subaru']
print(cars)
print("here is the original list:")
print(cars)
print("\nhere is sorted list:")
print(sorted(cars))
print(cars)