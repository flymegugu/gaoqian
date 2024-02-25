"""
Date: 2024-02-22 23:17:33
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-22 23:17:36
FilePath: /python/类/4-定制类和魔法方法/property.py
Description: 
"""
class Exam(object):
    def __init__(self,score):
        self._score=score
    def get_score(self):
        return self._score
    def set_score