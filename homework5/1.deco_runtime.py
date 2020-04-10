# -*- encoding: utf-8 -*-
'''
@File    :   1.runtime.py
@Time    :   2020/04/10 15:29:37
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#1  编写一个装饰器，能计算其他函数的运行时间；

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("该程序的运行时间为{0}毫秒".format(end_time - start_time))
    return wrapper

@timer
def test():
    time.sleep(2)
    print("fzs is a pig!!!")

test()