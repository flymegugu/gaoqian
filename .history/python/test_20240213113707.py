"""
Date: 2024-02-13 11:10:01
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-13 11:22:27
FilePath: /tools/python/test.py
Description: 
"""

test = [i for i in range(30) if i % 3 == 0]
print(test)

listdemo = ["google", "test"]
newdict = {key: len(key) for key in listdemo}
print(newdict)

setnew = {i**2 for i in (1, 2, 3)}
print(setnew)

a={x for x in 'asdfbasdfasdf' if x not in 'abc'}
print(a)
print(type(a))
a=(x for x in range(1,10))
