"""
Date: 2024-02-27 10:48:14
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-27 10:48:16
FilePath: /python/进程和线程/进程间通信1.py
Description: 
"""

from multiprocessing import Process, Queue


def write(q):
    print("process to write %s" % os.getpid())
    for value in ["A", "B", "C"]:
        print("put %s to queue...." % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print("process to read %s" % os.getpid())
    while True:
        value = q.get(True)
        print("get %s from queue" % value)
    