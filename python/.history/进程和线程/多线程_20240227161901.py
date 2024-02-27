"""
Date: 2024-02-27 16:16:40
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-27 16:16:47
FilePath: /python/进程和线程/多线程.py
Description: 
"""
from threading import Thread,current_thread

def thread_test(name):
    print('thread %s is running...' % current_thread().name)
    print('hello',name)