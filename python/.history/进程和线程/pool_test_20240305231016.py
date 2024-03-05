"""
Date: 2024-03-05 22:40:36
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-03-05 22:40:39
FilePath: /python/进程和线程/pool_test.py
Description: 
"""
from multiprocessing import Pool
import os,random,time

def long_time_task(name):
    print('run task %s (%s)'%(name,os.getpid()))