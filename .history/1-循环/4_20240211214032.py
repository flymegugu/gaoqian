n'''
Date: 2023-12-22 17:38:10
LastEditors: MaxGu flyme007@yeah.net
LastEditTime: 2023-12-23 16:02:46
FilePath: /tools/4.py
Description:  for 实例中使用了 break 语句，break 语句用于跳出当前循环体，不会执行 else 子句
'''
sites=["a","b","c","d"]
for site in sites:
    if site == "c":
        print("菜鸟教程")
        break
    print("循环数据" + site)
else:
     print("没有循环数据")
print("完成循环")
