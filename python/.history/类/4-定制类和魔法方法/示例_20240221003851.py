'''
Date: 2024-02-20 23:34:49
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-21 00:38:19
FilePath: /python/类/4-定制类和魔法方法/示例.py
Description: 
'''
class A(object):
    _dict=dict()
    def __new__(cls):
        if 'key' in A._dict:
            print('exist')
            return A._dict['key']
        else:
            print('new')
            return  object.__new__(cls)
    def __init__(self) -> None:
        pass
