"""
Date: 2024-02-27 17:06:14
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-27 17:06:26
FilePath: /python/进程和线程/锁.py
Description: 
"""
from threading import Thread,current_thread
num=0
def calc():
    global num
    print('thread %s is running...'% current_thread().name)
    