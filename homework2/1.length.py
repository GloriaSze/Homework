# -*- encoding: utf-8 -*-
'''
@File    :   1.count_length.py
@Time    :   2020/03/09 15:28:47
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#1 写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。

def get_len(n):
    return len(n)

choice = int(input("请选择要输入的数据类型（1.字符串 2.列表 3.元组）："))
if choice == 1:
    string = input("请输入该字符串：")
    print("该字符串的长度为：", get_len(string))
if choice == 2:
    string = input("请输入各项数据：")
    the_list = list(string)
    print("该列表的长度为：", get_len(the_list))
if choice == 3:
    string = input("请输入各项数据：")
    the_tuple = tuple(string)
    print("该元组的长度为：", get_len(the_tuple))