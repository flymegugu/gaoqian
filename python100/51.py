"""
Date: 2024-02-12 16:50:38
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-12 16:50:44
FilePath: /tools/python100/51.py
Description: 
"""
if __name__ == "__main__":
    a = 0x77
    b = a & 3
    print("a & b = %d" % b)
    b &= 7
    print("a & b = %d" % b)