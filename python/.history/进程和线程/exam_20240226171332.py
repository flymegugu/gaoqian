'''
Date: 2024-02-26 17:12:24
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 17:13:32
FilePath: /python/进程和线程/exam.py
Description: 
'''

from multiprocessing import Pool
imort os,time,random

def long_time_task(name):
    