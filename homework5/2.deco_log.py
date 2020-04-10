# -*- encoding: utf-8 -*-
'''
@File    :   2.deco_log.py
@Time    :   2020/04/10 15:40:00
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#2  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；

def log(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("程序被执行了")
    return wrapper

@log
def test():
    print("fzs is a big pig!!!!")

test()