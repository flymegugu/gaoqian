"""
Date: 2024-02-28 16:28:21
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-28 16:28:24
FilePath: /python/http/get.py
Description: 
"""

import requests,jsonpi

test = {"test": "23", "page": "2222"}
r = requests.get("http://httpbin.org/get", params=test)
print(r.url)

# 通过给 data 参数传递一个 dict，我们的数据字典在发出请求时会被自动编码为表单形式，比如：
payload={'test1':'test1','test2':'test2'}
r=requests.post('http://httpbin.org/post',data=payload)
print(r.text)
# 发送编码为 JSON 形式的数据
