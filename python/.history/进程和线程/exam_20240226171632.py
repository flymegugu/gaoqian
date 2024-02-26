'''
Date: 2024-02-26 17:12:24
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 17:16:09
FilePath: /python/进程和线程/exam.py
Description: 
'''

from multiprocessing import Pool
imort os,time,random

def long_time_task(name):
    print('run task %s (%s)...'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.radom()*3) 
    end=time.time()
    print('task %s runs %0.2f seconds'%(name,end-start))
    
