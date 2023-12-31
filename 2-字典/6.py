'''
Date: 2023-12-25 14:13:21
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2023-12-25 15:20:36
FilePath: /tools/2-字典/6.py
Description: 
'''

dict1 = {'user':'test','num':[1,2,3]}
print(id(dict1))
dict2 = dict1
print(id(dict2))
dict3=dict1.copy()
print(id(dict3))
print('hello')

dict1['user'] = 'root'
dict1['num'].remove(1)
print(dict1)
print(dict2)
print(dict3)

print("test")