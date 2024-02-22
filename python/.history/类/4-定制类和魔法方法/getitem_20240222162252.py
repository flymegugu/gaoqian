"""
Date: 2024-02-22 13:45:44
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-22 13:45:46
FilePath: /python/类/4-定制类和魔法方法/getitem.py
Description: 
"""
# class Fib(object):
#     def __getitem__(self,n):
#         a,b=1,1
#         for x in range(n):
#             a,b=b,a+b
#         return a


# fib=Fib()
# print(fib[0])
# print(fib[1])
# print(fib[2])
# class CustomClass:
#     def __init__(self, data):
#         self.data = data

#     def __getitem__(self, key):
#         return self.data[key]


# # 创建 CustomClass 的实例
# custom_obj = CustomClass([1, 2, 3, 4, 5])

# # 使用getitem 方法通过索引访问
# print(custom_obj[1])
class Fib(object):
    def __getitem__(self,n):
        if isinstance(n,slice):
            a,b=1,1
            start,stop=n.start,n.stop
            L=[]
            for i in range(stop):
                if i>= start:
                    L.append(a)
                a,b=b,a+b
            return L
        if isinstance(n,int):
            a,b=1,1
            for i in range(n):
                a,b=b,a+b
            return a