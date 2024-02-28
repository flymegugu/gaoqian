"""
Date: 2024-02-28 09:46:36
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-28 09:46:55
FilePath: /python/进程和线程/threadlocal.py
Description: 
"""
from threading import Thread,current_thread

def echo(num):
    print(current_thread().name,num)
def calc():
    print('thread  %s is running...'% current_thread().name)
    local_num=0
    for _ in range(100000):
        local_num+=1
    echo(local_num)
    print('thread %s ended'% current_thread().name)

if __name__=='__main__':
    print('thread %s is running...'% current_thread().name)
    thread=[]
    for i in range(5):
        threads.append(Thread(target=calc))
        threads[i].