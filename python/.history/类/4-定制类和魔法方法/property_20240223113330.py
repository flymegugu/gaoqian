"""
Date: 2024-02-22 23:17:33
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-22 23:17:36
FilePath: /python/类/4-定制类和魔法方法/property.py
Description:@property 把方法『变成』了属性。
我们给方法 score 加上了 @property，于是我们可以把 score 当成一个属性来用，此时，又会创建一个新的装饰器 score.setter，它可以把被装饰的方法变成属性来赋值。

另外，我们也不一定要使用 score.setter 这个装饰器，这时 score 就变成一个只读属性了： 
"""

# class Exam(object):
#     def __init__(self, score):
#         self._score = score

#     def get_score(self):
#         return self._score

#     def set_score(self, val):
#         if val < 0:
#             self._score = 0
#         elif val > 100:
#             self._score = 100
#         else:
#             self._score = val


# e = Exam(-1)
# print(e.get_score())
print("###############")


class Exam(object):
    def __init__(self,score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val


e = Exam(60)
print(e.score)
e.score=200
print(e.score)
