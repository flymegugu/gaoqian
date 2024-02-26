"""
Date: 2024-02-26 17:39:52
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 17:45:40
FilePath: /python/进程和线程/多进程1.py
Description: 
"""

import os

print("process (%s) start....." % os.getpid())
pid = os.fork()
print(pid)
if pid == 0:
    print("i am child process (%s) and my parent is %s." % (os.getpid(), os.getppid()))
else:
    print('i (%s) just created a child process (%s)'%s)