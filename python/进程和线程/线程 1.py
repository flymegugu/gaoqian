"""
Date: 2024-03-04 23:22:15
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-03-04 23:37:27
FilePath: /python/进程和线程/线程 1.py
Description: 
"""

"""
Date: 2024-03-04 23:22:15
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-03-04 23:26:31
FilePath: /python/进程和线程/线程 1.py
Description: 
"""

import time, threading


def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("thread %s >>> %s" % (threading.current_thread(), n))
        time.sleep(1)
    print("thread %s is running..." % threading.current_thread().name)


print("theattttttttttd %s is running..." % threading.current_thread().name)
t = threading.Thread(target=loop, name="LoopThread")
t.start()
t.join()
print("thread %s ended" % threading.current_thread().name)
