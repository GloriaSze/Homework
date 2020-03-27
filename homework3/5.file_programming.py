# -*- encoding: utf-8 -*-
'''
@File    :   4.file_programming.py
@Time    :   2020/03/26 21:16:43
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#5 文件编程小项目

with open(r'E:\Study\Year2_2nd\Python\PythonWorkspace\homework3\blowing in the wind.txt', 'r') as file:
    lyrics_list = []
    for i in file.readlines():
        line = i.strip()
        lyrics_list.append(line)
    lyrics_list.insert(0, 'Blowin’ in the wind')
    lyrics_list.insert(1, 'Bob Dylan')
    lyrics_list.append('1962 by Warner Bros. Inc.')
    for i in lyrics_list:
        print(i)