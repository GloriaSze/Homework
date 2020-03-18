# -*- encoding: utf-8 -*-
'''
@File    :   list_same element.py
@Time    :   2020/03/06 16:20:05
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#3 定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；

list1=['P', 'y', 't', 'h', 'o', 'n', 'e']
list2=['V', 'S', 'c', 'o', 'd', 'e', 'n']

print("两个列表中相同的的元素有：", list(x for x in list1 if x in list2))