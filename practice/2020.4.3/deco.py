# -*- encoding: utf-8 -*-
'''
@File    :   deco.py
@Time    :   2020/04/03 09:39:58
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

def record(func):
    def wrapper(*args):
        print("加法被执行了")
        func(*args)
    return wrapper

@record
def sum(a, b):
    print(a + b)

a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
sum(a, b)