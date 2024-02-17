"""
Date: 2024-02-18 01:03:07
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-02-18 01:22:44
FilePath: /tools/python/装饰器.py
Description: 
"""

"""
Date: 2024-02-18 01:03:07
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-02-18 01:14:04
FilePath: /tools/python/装饰器.py
Description: ()
"""

"""
Date: 2024-02-18 01:03:07
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-02-18 01:03:10
FilePath: /tools/python/装饰器.py
Description: 
"""


def hello():
    return "hello world"


def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"

    return wrapped

makeitalic