# -*- encoding: utf-8 -*-
'''
@File    :   4.communication.py
@Time    :   2020/04/28 19:43:47
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#4 多进程通讯：
#  编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；

from multiprocessing import Process, Queue
import os, time

def writer(q, info):
    print("writer已启动：{0}".format(os.getpid()))
    q.put(info)
    print("您已发送信息：{0}".format(info))
    time.sleep(1)

def reader(q):
    print("Reader已启动：{0}".format(os.getpid()))
    while True:
        info = q.get(True)
        print("您已收到信息：{0}".format(info))

def main():
    info = input("请输入您想要发送的信息：")
    q = Queue()
    p_write = Process(target = writer, args = (q, info,))
    p_read = Process(target = reader, args = (q,))
    p_write.start()
    p_read.start()
    p_write.join()
    p_read.terminate()

if __name__ == '__main__':
    main()