# -*- encoding: utf-8 -*-
'''
@File    :   change_suffix.py
@Time    :   2020/03/26 20:35:11
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#4 题目要求：
#  在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
#  将当前img目录所有以.png结尾的后缀名改为.jpg.#

import os

path = r'E:\Study\Year2_2nd\Python\PythonWorkspace\homework3\img'
png_list = os.listdir(path)
for i in png_list:
    old_name = os.path.join(path, i)
    new_name = os.path.join(path, old_name.replace('.png', '.jpg'))
    os.rename(old_name, new_name)