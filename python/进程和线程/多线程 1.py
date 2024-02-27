"""
Date: 2024-02-27 16:56:46
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-27 16:56:52
FilePath: /python/进程和线程/多线程 1.py
Description:我们创建了一个线程对象，并通过调用 start 方法启动线程的执行。线程会在 worker 函数中执行具体的工作。然后，我们调用线程的 join 方法来等待线程完成。最后，主线程继续执行。 
"""

import threading


def worker():
    print(f"线程{threading.Thread.name} 开始执行")
    for i in range(5):
        print(f"线程 {threading.Thread.name}：执行工作{i}")
    print(f"线程 {threading.Thread.name} 执行完毕")


thread = threading.Thread(target=worker)
thread.start()
thread.join()
print("主线程执行完毕")
