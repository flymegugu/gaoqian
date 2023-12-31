'''
Date: 2023-12-26 13:52:36
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2023-12-29 09:35:07
FilePath: /tools/3-迭代生成/2.py
Description: 
'''

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)