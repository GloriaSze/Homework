# -*- encoding: utf-8 -*-
'''
@File    :   2.sum.py
@Time    :   2020/03/09 15:47:16
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#2 编写一个函数,接收n个数字，求这些参数数字的和;

def get_sum(l):
    sum_num = sum(l)
    return sum_num

n = input("请输入各个数字，以空格隔开：")
the_list = n.split(" ")
numlist = []
for i in the_list:
    numlist.append(int(i))
print("和为：", get_sum(numlist))
