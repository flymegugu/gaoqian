"""
Date: 2024-02-07 18:32:24
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-02-07 18:33:57
FilePath: /work_tools/Users/maxgu/Desktop/MaxGu/tools/python100/test.py
Description: 
"""

def func(g,arr):
    return([g(x) for x in arr])

def double(x):
    return 2 * x


def test2(x):
    return(x * x)
arr1 = func(double,[1,2,3,4])
arr2 = func(test2,[1,2,3,4])
print(arr1,arr2)
