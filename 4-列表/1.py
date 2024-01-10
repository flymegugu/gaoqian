'''
Date: 2024-01-02 12:56:47
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2024-01-09 00:02:19
FilePath: /tools/4-列表/1.py
Description: 
'''
def spam():
    global eggs
    eggs = '1111'
def bacon():
    eggs = 'baco'
def ham():
    print(eggs)
eggs = 42
spam()
print(eggs)
