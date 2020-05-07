# -*- encoding: utf-8 -*-
'''
@File    :   4.chatting_room.py
@Time    :   2020/05/07 16:48:10
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#4 设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室；

import socket
import threading
import os
import getinfo

class Server():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (getinfo.get_ip(), 10000)
        self.users = {}

    def start_server(self):
        try:
        	self.sock.bind(self.addr)
        except Exception as e:
        	print(e)
        self.sock.listen(5)
        print("服务器已开启，等待连接...")
        print("在空白处输入stop server并回车，来关闭服务器")
        self.accept_cont()

    def accept_cont(self):
        while True:
            s, addr = self.sock.accept()
            self.users[addr] = s
            number = len(self.users)
            print("用户{}连接成功！现在共有{}位用户".format(addr, number))

            threading.Thread(target = self.recv_send, args = (s, addr)).start()
    
    def recv_send(self, sock, addr):
        while True:
            try:
                response = sock.recv(4096).decode("gbk")
                msg = "{}用户{}发来消息：{}".format(getinfo.get_time(), addr, response)

                for client in self.users.values():
                    client.send(msg.encode("gbk"))
            except ConnectionResetError:
                print("用户{}已经退出聊天！".format(addr))
                self.users.pop(addr)
                break

    def close_server(self):
        for client in self.users.values():
            client.close()
        self.sock.close()
        os._exit(0)

if __name__ == "__main__":
    server = Server()
    server.start_server()
    while True:
        cmd = input()
        if cmd == "stop server":
            server.close_server()
        else:
            print("输入命令无效，请重新输入！")