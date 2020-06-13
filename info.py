# -*- coding: utf-8 -*-
import os


# 获取时间
def get_date():
    command = 'echo %date%'  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.read()
    info.strip()
    info = info.replace("周一", "Mon.")
    info = info.replace("周二", "Tue.")
    info = info.replace("周三", "Wed.")
    info = info.replace("周四", "Thu.")
    info = info.replace("周五", "Fri.")
    info = info.replace("周六", "Sat.")
    info = info.replace("周日", "Sun.")
    return info


# 获取系统信息
def get_sys_info():
    command = 'systeminfo'
    r = os.popen(command)
    info = r.read()
    info.strip()
    return info


# 获取网卡信息
def get_nic_info():
    command = 'ipconfig /all'
    r = os.popen(command)
    info = r.read()
    info.strip()
    return info


# 获取路由表
def get_routing_info():
    command = 'route print'
    r = os.popen(command)
    info = r.read()
    info.strip()
    return info


# 查看arp表
def get_arp_info():
    command = 'arp -a'
    r = os.popen(command)
    info = r.read()
    info.strip()
    return info


# 查看端口信息
def get_conn_info():
    command = 'netstat -ano'
    r = os.popen(command)
    info = r.read()
    info.strip()
    return info


# 获取用户信息
def get_user_info():
    command = 'net user'
    r = os.popen(command)
    info = r.read()
    info.strip()
    return info


# 查看进程信息
def get_process_info():
    command = 'tasklist /v'
    r = os.popen(command)
    info = r.read()
    info.strip()
    return info


# 查看句柄信息
def get_file_handle():
    command = 'handle64.exe'
    r = os.popen(command)
    info = r.read()
    info.strip()
    return info


# 获取硬盘信息
def get_disk_info():
    command = 'diskext64.exe'
    r = os.popen(command)
    info = r.read()
    info.strip()
    return info


# 获取服务信息
def get_service_info():
    command = 'sc query state= all'
    r = os.popen(command)
    info = r.read()
    info.strip()
    return info
