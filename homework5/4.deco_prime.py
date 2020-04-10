# -*- encoding: utf-8 -*-
'''
@File    :   4.deco_prime.py
@Time    :   2020/04/10 16:18:00
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#4  编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
#     三个目标函数分别为：
#     A 打印输出20000之内的素数；
#     B 计算整数2-10000之间的素数的个数；
#     C 计算整数2-M之间的素数的个数；

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def void_func(func):
    def wrapper():
        func()
    return wrapper

def return_func(func):
    def wrapper():
        res = func()
        return res
    return wrapper

def para_func(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper

@void_func
def print_prime():
    print("20000之内的素数有：")
    for i in range(0, 20001):
        if is_prime(i):
            print(i, end = ' ')

@return_func
def prime_count():
    count = 0
    for i in range(0, 10001):
        if is_prime(i):
            count += 1
    return count

@para_func
def print_count2(n):
    count = 0
    for i in range(0, n+1):
        if is_prime(i):
            count += 1
    return count

print_prime()
print("\n2-10000之间的素数有{0}个".format(prime_count()))
m = int(input("请输入M的数值："))
print("2-{0}之间的素数有{1}个".format(m, print_count2(m)))