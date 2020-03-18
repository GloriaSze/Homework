# -*- encoding: utf-8 -*-
'''
@File    :   file_read.py
@Time    :   2020/03/18 15:53:02
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

# 练习3:   一个文件内容的如下,请读取文件的内容, 并输出;
#           姓名      学号      分数
#           张三      101         78
#           李四      102         87
#           王五       103        83

f = open(r'C:\Users\Gloria\Desktop\student.txt', 'r', encoding = 'UTF8')

f_list = f.readlines()

for i in f_list:
    i.strip()
    print(i)