# -*- encoding: utf-8 -*-
'''
@File    :   cal.py
@Time    :   2020/04/01 08:33:32
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

def sum(a, b):
    return a + b

def minus(a, b):
    return a - b

def times(a, b):
    return a * b

def over(a, b):
    return a / b

def test(a, b, func):
    print(func(a, b))

a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
choice = int(input("请选择要实现的运算（1.加 2.减 3.乘 4.除）："))
if choice == 1:
    test(a, b, sum)
elif choice == 2:
    test(a, b, minus)
elif choice == 3:
    test(a, b, times)
elif choice == 4:
    test(a, b, over)

