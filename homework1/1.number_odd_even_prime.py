# -*- encoding: utf-8 -*-
'''
@File    :   number_odd_even_prime.py
@Time    :   2020/03/06 15:09:59
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#1 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

list_prime=[]
for x in range(0, 51):
    if is_prime(x):
        list_prime.append(x)

print("0-50之间的偶数是：", list(x for x in range(0, 51) if x % 2 == 0))
print("0-50之间的奇数是：", list(x for x in range(0, 51) if x % 2 == 1))
print("0-50之间能同时被2和3整除的数：", list(x for x in range(0, 51) if x % 2 == 0 and x % 3 == 0))
print("0-50之间的质数是：", list_prime)