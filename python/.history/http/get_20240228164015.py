"""
Date: 2024-02-28 16:28:21
LastEditors: flymegugu flyme007@yeah.net
LastEditTime: 2024-02-28 16:28:24
FilePath: /python/http/get.py
Description: 
"""

import requests

test = {"test": "23", "page": "2222"}
r = requests.get("http://httpbin.org/get", params=test)
print(r.url)


payload=''