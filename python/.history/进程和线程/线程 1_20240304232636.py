'''
Date: 2024-03-04 23:22:15
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-03-04 23:26:31
FilePath: /python/进程和线程/线程 1.py
Description: 
'''

import time,threading

def loop():
    print('thread %s is running...'% threading.current_thread().name)
    n=0
    while n <5:
        n+=1
        print('thread %s >>> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s is running...'% threading.current_thread().name)
print('thead %s is running...'% threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
