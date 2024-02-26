"""
Date: 2024-02-26 17:12:24
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 17:17:12
FilePath: /python/进程和线程/exam.py
Description: 
"""

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print("run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.radom() * 3)
    end = time.time()
    print("task %s runs %0.2f seconds" % (name, (end - start)))
if __name__=='__main__':
    print('parent process %s'% os.getpid())
    p=Pool(4)
    for i in range(5):
        print