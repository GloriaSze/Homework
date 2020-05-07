# -*- encoding: utf-8 -*-
'''
@File    :   4.get_ip_time.py
@Time    :   2020/05/07 18:40:00
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#4 设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室；

import socket
import datetime

def get_ip():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip

def get_time():
    now = datetime.datetime.now()
    send_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return send_time
