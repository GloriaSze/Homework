# -*- encoding: utf-8 -*-
'''
@File    :   copy.py
@Time    :   2020/03/25 08:42:18
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

import os, sys

def copy_file(p1, p2):
    try:
        with open(p1, 'r') as file1:
            content = file1.read()
        with open(p2, 'w') as file2:
            file2.write(content)
    except FileNotFoundError as err:
        print(err)

path1 = r'E:\Study\Year2_2nd\Python\PythonWorkspace\practice\2020.3.25\old_file.txt'
path2 = r'E:\Study\Year2_2nd\Python\PythonWorkspace\practice\2020.3.25\new_file.txt'
copy_file(path1, path2)