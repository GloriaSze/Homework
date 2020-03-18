# -*- encoding: utf-8 -*-
'''
@File    :   random.py
@Time    :   2020/03/06 16:39:58
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#5  使用random模块，生成随机数，来初始化一个列表，元组；
#   使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法；

import random

list_random = [random.randint(0, 20) for x in range(10)]
print(list_random)
print(tuple(list_random))