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
    start=time.time()
    time.sleep(random.random()*10)
    end=time.time()
    print('task %s runs %0.2f'%(name,(end-start)))

if __name__=='__main__':
    print('parent process %s'% os.getpid())
    p=Pool(10)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
        