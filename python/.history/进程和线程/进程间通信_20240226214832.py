'''
Date: 2024-02-26 21:42:30
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 21:48:25
FilePath: /python/进程和线程/进程间通信.py
Description: 
'''
from multiprocessing import Process,Queue

def write_task(q):
    try:
        n=1
        while n<5:
            print('write %d'%n)
