# -*- encoding: utf-8 -*-
'''
@File    :   get_list_odd.py
@Time    :   2020/03/09 16:07:46
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#3  编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#   数字列表请用随机数函数生成;

import random

def get_odd(numlist):
    oddlist = []
    for i in numlist:
        if i % 2 == 1:
            oddlist.append(i)
    return oddlist

size = 10
numlist = []
for i in range(size):
    numlist.append(random.randint(1, 100))
print("列表中的奇数为：", get_odd(numlist))