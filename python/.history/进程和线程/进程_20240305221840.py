"""
Date: 2024-03-05 22:16:33
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-03-05 22:16:37
FilePath: /python/进程和线程/进程.py
Description: 
"""
import os
print('process %s start'% os.getpid())
pid=os.fork()
print(pid) #子进程且返回0
print(os.getpid)
# if pid ==0:
    print('i am child process %s and my parent is %s'%(os.getpid))
