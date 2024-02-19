"""
Date: 2024-02-19 13:36:55
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-19 13:36:58
FilePath: /tools/python/函数式编程/5-会打扮的装饰器/1.py
Description: 
"""
class Store(object):
    def get_food(self,username,food):
        if username !='admin':