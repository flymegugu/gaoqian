#!/bin/bash
##
@Date: 2024-01-26 10:45:50
 @LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 @LastEditTime: 2024-01-30 09:42:55
 @FilePath: /work_tools/ansible/test_playbook/roles/d3_扩容/files/proxy_ck_ports.sh
@Description:
##
port_array=(8089 8084 8091 10022 10007 10080)
service_array=(passic locic commonconf)

for ((i = 0; i < ${#port_array[@]}; i++)); do
    time=$(date "+%Y-%m-%d %H:%M:%S")
    port=${port_array[i]}
    service_name=${service_array[i]}
    port_status=$(netstat -nlt | grep ${port_array[i]} | wc -l)
    service_process_num=$(pgrep -l $service_name | wc -l)

    if [ $port_status -lt 1 ]; then
        #echo -e "\033[32m[未占用] $time $service_process_num $service_name:$port\033[0m"
        echo -e "[端口不存在] $time $service_process_num $service_name:$port"
    else
        echo -e "[端口存在] $time $service_process_num $service_name:$port"
    fi
done
