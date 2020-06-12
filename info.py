# -*- coding: utf-8 -*-
import os


def get_date():
    command = 'echo %date%'  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.read()
    info.strip("\r\n")
    info = info.replace("周一", "Mon.")
    info = info.replace("周二", "Tue.")
    info = info.replace("周三", "Wed.")
    info = info.replace("周四", "Thu.")
    info = info.replace("周五", "Fri.")
    info = info.replace("周六", "Sat.")
    info = info.replace("周日", "Sun.")
    return info
    print(type(info))


def get_sys_info():
    command = 'systeminfo'  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.read()
    info.strip("\r\n")
    return info


def get_nic_info():
    command = 'ipconfig /all'  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.read()
    return info


def get_routing_info():
    command = 'route print'  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.read()
    info.strip("\r\n")
    return info


def get_arp_info():
    command = 'arp -a'  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.read()
    info.strip("\r\n")
    return info


def get_conn_info():
    command = 'netstat -ano'  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.read()
    info.strip("\r\n")
    return info


def get_user_info():
    command = 'net user'  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.read()
    info.strip("\r\n")
    return info


def get_process_info():
    command = 'tasklist /v'  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.read()
    info.strip("\r\n")
    return info


def get_file_handle():
    command = 'handle64.exe'  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.read()  # 读取命令行的输出到一个list
    info.strip("\r\n")
    return info


def get_disk_info():
    command = 'diskext64.exe'  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.read()  # 读取命令行的输出到一个list
    info.strip("\r\n")
    return info


def get_service_info():
    command = 'sc query state= all'  # 可以直接在命令行中执行的命令
    r = os.popen(command)  # 执行该命令
    info = r.read()
    info.strip("\r\n")
    return info
