# -*- encoding: utf-8 -*-
'''
@File    :   3.udp_client.py
@Time    :   2020/05/07 16:22:19
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()