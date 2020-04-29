# -*- encoding: utf-8 -*-
'''
@File    :   3.prime.py
@Time    :   2020/04/28 19:10:20
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#3  多进程练习：
#计算1～100000之间所有素数的个数， 要求如下:
#- 编写函数判断一个数字是否为素数，然后统计素数的个数；
#-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
#-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。

import time
from multiprocessing import Pool

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def speed_withPool(num):
    pool = Pool(num)
    start_time = time.time()
    count = 0
    for i in range(1, 100000):
        if pool.apply(is_prime, args = (i,)) == True:
            count += 1
    pool.close()
    pool.join()
    print("1-100000之间的素数有{0}个".format(count))
    end_time = time.time()
    print("用{0}个多进程的运行时间为：{1}".format(num, end_time - start_time))

def speed_withoutPool():
    start_time = time.time()
    count = 0
    for i in range(1, 100000):
        if is_prime(i):
            count += 1
    print("1-100000之间的素数有{0}个".format(count))
    end_time = time.time()
    print("不用多进程的运行时间为{0}".format(end_time - start_time))

def main():
    speed_withoutPool()
    speed_withPool(4)
    speed_withPool(10)

if __name__ == '__main__':
    main()