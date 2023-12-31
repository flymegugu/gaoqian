# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 批量测试端口号
import sys
import telnetlib


def telnet(host, port):
    """
    测试端口号通不通
    :return:
    """
    try:
    	#  timeout单位s
        telnetlib.Telnet(host=host, port=port, timeout=2)
        print(f"{port}  端口开放")
    except:
        print(f"{port}  端口未开放")
        # 或什么都不打印
        # pass

def for_port():
    """
    添加端口到列表中
    使用示例: python3 telnet_for.py 39.105.137.91 81 82 83 84
    :return:
    """
    host = sys.argv[1]

    port_list = sys.argv[2:]
    if not len(port_list):
        #port_list = [39901,39903,39905,39906,39907,39908,39910,39911,39912,39913]
        port_list = [9901,9902,9904,9906,9907,9908,9910,9911,9912,9913,9914,80]
    for port in port_list:
        telnet(host, port)


if __name__ == '__main__':
    for_port()

