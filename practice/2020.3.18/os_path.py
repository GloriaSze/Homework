# -*- encoding: utf-8 -*-
'''
@File    :   os_path.py
@Time    :   2020/03/18 15:20:20
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# 练习1:  在window平台下练习os.path 相关方法的使用

import os

filepath = r'E:\Study\Year2_2nd\Python\PythonWorkspace\practice\2020.3.18\student.txt'

print("文件名：", os.path.basename(filepath) )   # 返回文件名
print("目录路径：", os.path.dirname(filepath) )    # 返回目录路径
print("分割文件名与路径：", os.path.split(filepath) )      # 分割文件名与路径
print("合成路径：", os.path.join(filepath) )  # 将目录和文件名合成一个路径