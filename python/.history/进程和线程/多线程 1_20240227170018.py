"""
Date: 2024-02-27 16:56:46
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-27 16:56:52
FilePath: /python/进程和线程/多线程 1.py
Description: 
"""
import threading
def worker():
    print(f'线程{threading.Thread.name} 开始执行')
    for i in range(5):
        print(f'线程 {threading.Thread.name}：执行工作{i}')
    print(f"线程 {threading.Thread.name} 执行完毕")

thread=threading.Thread(target=worker)
thread.start()
tread.join()
print("")