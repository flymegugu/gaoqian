"""
Date: 2024-03-05 22:29:57
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-03-05 22:30:00
FilePath: /python/进程和线程/多进程 2.py
Description: 
"""
from multiprocessing import Process
import os
def run_poc(name):
    print('子进程是%s,%s')
