# -*- encoding: utf-8 -*-
'''
@File    :   4.str_count.py
@Time    :   2020/03/09 16:23:09
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#4  写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;

def count(string):
    character = number = space = other = 0
    for i in string:
        if i.isdigit() == True:
            number += 1
        elif i.isalpha() == True:
            character += 1
        elif i.isspace() == True:
            space += 1
        else:
            other += 1
    print("该字符串的字母有", character, "个；数字有", number, "个；空格有", space, "个；其他字符有：", other, "个")

string = input("请输入字符串：")
count(string)