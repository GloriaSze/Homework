# -*- encoding: utf-8 -*-
'''
@File    :   6.Fibonacci.py
@Time    :   2020/03/10 10:39:12
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#6  定义一个函数, 打印输出n以内的斐波那契数列;

n = int(input("请输入n的值："))

def fibo():
    a, b = 0, 1
    print(a, end = ' ')
    while a+b <= n:
        a, b = b, a+b
        print(b, end = ' ')

fibo()