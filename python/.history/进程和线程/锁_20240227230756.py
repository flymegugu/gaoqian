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
    for _ in range(10000):
        num += 1
    print('thread %s ended'% current_thread().name)

if __name__=='__main__':
    print('thread %s is running...'% current_thread().name)
    thread=[]
    for i in range(5):
        threads.append(Thread(target=calc))
        thread[i].start()
    for i in range(5):
        