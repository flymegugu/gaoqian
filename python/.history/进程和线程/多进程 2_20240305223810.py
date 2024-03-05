"""
Date: 2024-03-05 22:29:57
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-03-05 22:30:00
FilePath: /python/进程和线程/多进程 2.py
Description: 
"""

from multiprocessing import Process
import os


def run_poc(name):
    print("子进程是%s,%s" % (name, os.getpid()))
    print(
        "hello i am child"
    )  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

if __name__=='__main__':
    print('parent process %s'% os.getpid())
    p=Process(target=run_poc,args=('testtest',))
    p.start()
    p.join()
    print('child process end')
