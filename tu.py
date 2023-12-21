'''
Author: MaxGu
Date: 2023-12-18 13:29:50
LastEditTime: 2023-12-21 16:36:39
FilePath: /tools/tu.py
Description: 

'''
import matplotlib.pyplot as plt
import numpy as np

# 生成一些随机数据
x = np.random.rand(10)
y = np.random.rand(10)

# 创建一个散点图
plt.scatter(x, y)

# 显示图表
plt.show()
