"""
Date: 2024-02-27 17:06:14
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-27 17:06:26
FilePath: /python/进程和线程/锁.py
Description: 
"""

from threading import Thread, current_thread,Lock


num = 0
lock=Lock()

def calc():
    global num
    print("thread_calc %s is running..." % current_thread().name)
    for _ in range(1000000):
        # lock.acquire()
        num += 1
        lock.release()
    print("thread_calc %s ended" % current_thread().name)


if __name__ == "__main__":
    print("thread %s is running..." % current_thread().name)
    threads= []
    for i in range(5):
        threads.append(Thread(target=calc))
        threads[i].start()
    for i in range(5):
        threads[i].join()
    print("global num:%d" % num)
    print("thread %s ended:" % current_thread().name)
