"""
Date: 2024-02-28 10:49:55
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-28 10:49:58
FilePath: /python/进程和线程/线程使用自己的局部变量.py
Description: 
"""
from threading import Thread, current_thread

global_dict = {}

def echo():
    num = global_dict[current_thread()]    # 线程根据自己的 ID 获取数据
    print(current_thread().name, num)

def calc():
    print ('thread %s is running...' % current_thread().name

    global_dict[current_thread()] = 0
    for _ in xrange(10000):
        global_dict[current_thread()] += 1
    echo()

    print 'thread %s ended.' % current_thread().name

if __name__ == '__main__':
    print 'thread %s is running...' % current_thread().name

    threads = []
    for i in range(5):
        threads.append(Thread(target=calc))
        threads[i].start()
    for i in range(5):
        threads[i].join()

    print 'thread %s ended.' % current_thread().name