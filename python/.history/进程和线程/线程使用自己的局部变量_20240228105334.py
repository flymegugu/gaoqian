"""
Date: 2024-02-28 10:49:55
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-28 10:49:58
FilePath: /python/进程和线程/线程使用自己的局部变量.py
Description: 
"""
from threading import Thread,current_thread

global_dict={}
def echo():
    num=global_dict[current_thread()]
    print(current_thread().name,num)

def calc():
    print('thread %s is running...'% current_thread().name)
    global