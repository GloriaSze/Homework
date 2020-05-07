# -*- encoding: utf-8 -*-
'''
@File    :   3.udp_server.py
@Time    :   2020/05/07 16:16:16
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('Bind UDF on 9999...')

while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)