# -*- encoding: utf-8 -*-
'''
@File    :   2.read.py
@Time    :   2020/03/24 14:53:17
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx

def read_txt():
    content_list = []
    try:
        with open(r'E:\Study\Year2_2nd\Python\PythonWorkspace\homework3\input.txt', 'r') as file:
            for i in file:
                content_list.append(i.strip())
    except FileNotFoundError as err:
        print('OSError:{0}'.format(err))
    print(content_list)
    return content_list

def print_list(list):
   l = enumerate(list, start = 1)
   for line, content in l:
       print('第{0}行：{1}'.format(line, content))

print_list(read_txt())