# -*- encoding: utf-8 -*-
'''
@File    :   1.queue.py
@Time    :   2020/03/31 20:30:48
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#1 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；
#  用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
#  提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)

from collections import deque
import time

def list_insert():
    list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for i in range(100):
        list.insert(0, i)
    for i in range(100):
        list.append(i)

def queue_insert():
    list = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    list.appendleft('head')
    list.appendleft('tail')

list_start_time = time.time()
list_insert()
list_end_time = time.time()
list_time = list_end_time - list_start_time
print("列表自带的函数所需时间为：", list_time)

queue_start_time = time.time()
queue_insert()
queue_end_time = time.time()
queue_time = queue_end_time - queue_start_time
print("deque所需的时间为：",queue_time )

print("两者时间差为：", list_time - queue_time)