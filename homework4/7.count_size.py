# -*- encoding: utf-8 -*-
'''
@File    :   7.count_size.py
@Time    :   2020/04/06 20:21:38
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#7 使用python代码统计一个文件夹中所有文件的总大小

import os

folder = r'E:\Study\Year2_2nd\Python\PythonWorkspace\practice'
total_size = 0

def sum(path):
    file_list = os.listdir(path)
    for i in file_list:
        new_path = path + '\\' + i
        if os.path.isfile(new_path):
            global total_size
            total_size += os.path.getsize(new_path)
        else:
            sum(new_path)
    return total_size
 
print('该文件夹的大小为{0}字节'.format(sum(folder)))