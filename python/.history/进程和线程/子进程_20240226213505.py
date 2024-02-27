"""
Date: 2024-02-26 17:52:46
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-26 21:30:47
FilePath: /python/进程和线程/子进程.py
Description: 
"""

import subprocess
print('$ nslookup www.python.org')
subprocess.call(['nslookup','www.python.org'])
print('exit code',r)