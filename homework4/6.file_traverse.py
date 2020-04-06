# -*- encoding: utf-8 -*-
'''
@File    :   6.file_traverse.py
@Time    :   2020/04/06 18:07:37
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#6  通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
#   名称         日期                   类型（文件夹或者 文件）       大小

import os, datetime

folder = r'E:\Study\Year2_2nd\Python\PythonWorkspace\practice'
name_list = []
file_list = []

for file in os.listdir(folder):
    name_list.append(file)
for i in range(len(name_list)):
    file_info = []
    file_info.append(name_list[i])
    path = folder + '\\' + name_list[i]
    time = datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime('%Y-%m-%d %H:%M:%S')
    file_info.append(time)
    if os.path.isfile(path):
        file_info.append('文件')
        file_info.append(os.path.getsize(path))
    else:
        file_info.append('文件夹')
    file_list.append(file_info)

print("名称\t\t日期\t\t\t类型\t\t大小")
for i in file_list:
    if i[2] is '文件夹':
        print(i[0] + '\t' + i[1] + '\t' + i[2] + '\t')
    else:
        print(i[0] + '\t' + i[1] + '\t' + i[2] + '\t\t' + str(i[3])+'字节')