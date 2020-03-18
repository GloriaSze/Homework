# -*- encoding: utf-8 -*-
'''
@File    :   Fibonacci.py
@Time    :   2020/03/06 18:58:55
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#6  前面2个元素为0，1，输出100以内的斐波那契数列；

n = 100

def fibo():
    a, b = 0, 1
    print(a, end = ' ')
    while a+b <= n:
        a, b = b, a+b
        print(b, end = ' ')

fibo()