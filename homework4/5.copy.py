# -*- encoding: utf-8 -*-
'''
@File    :   5.copy.py
@Time    :   2020/04/06 17:42:47
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#5  通过Python来模拟实现一个txt文件的拷贝过程;

def copy_txt():
    try:
        with open('original_file.txt', 'r') as file1:
           content_list = file1.readlines()
        with open('copy_file.txt', 'w') as file2:
            file2.writelines(content_list)
    except FileNotFoundError as err:
        print('FileNotFoundError:{0}'.format(err))

copy_txt()