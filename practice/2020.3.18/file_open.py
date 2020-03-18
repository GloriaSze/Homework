# -*- encoding: utf-8 -*-
'''
@File    :   file_open.py
@Time    :   2020/03/18 15:26:02
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# 练习2:  构造上述文件结构,分别在指定位置打开文件进行写入操作;
# 同级文件夹里面打开;  同级目录下的子目录里面打开; 上一级文件目录中的其他文件夹中打开

# here put the import lib

f = open(r'E:\Study\Year2_2nd\Python\PythonWorkspace\practice\2020.3.18\student.txt')
with open(r'..\b_file\file_open2.txt',"r") as file:
    print(file.readlines())