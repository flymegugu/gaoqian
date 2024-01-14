'''
Date: 2024-01-13 22:16:12
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-01-14 16:55:55
FilePath: /tools/python100/11.py
Description: 
'''
def get_rabbit_num(month):
    if month < 3:
        # 前两个月兔子的数量
        return month
    else:
        # 第三个月及以后的兔子数量
        return get_rabbit_num(month - 1) + get_rabbit_num(month - 2)

# 测试代码
if __name__ == '__main__':
    print(get_rabbit_num(6))