"""
Date: 2024-02-26 16:20:21
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 16:24:00
FilePath: /python/文件和目录/3-os模块/exam.py
Description: 
"""

import os

# print(
#     os.path.basename(
#         "/Users/maxgu/Desktop/MaxGu/tools/python/文件和目录/3-os模块/exam.py"
#     )
# )

# print(
#     os.path.split(
#         "/Users/maxgu/Desktop/MaxGu/tools/python/文件和目录/3-os模块/exam.py"
#     )
# )

for root, dirs, files in os.walk(
    "/Users/maxgu/Desktop/MaxGu/tools/python/文件和目录/3-os模块/exam.py"):
    print(root)
