# -*- encoding: utf-8 -*-
'''
@File    :   dict_pickle.py
@Time    :   2020/03/18 19:39:16
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# 练习5:给定一个字典,保存了5个同学的学号,姓名,年龄;使用pickle模块将数据对象保存到文件中去;

import pickle

stu = {
    '01': {'Name': 'Ada', 'Number': 100, 'Age': 18},
    '02': {'Name': 'Bob', 'Number': 101, 'Age': 19},
    '03': {'Name': 'Cathy', 'Number': 102, 'Age': 19},
    '04': {'Name': 'Daisy', 'Number': 103, 'Age': 19},
    '05': {'Name': 'Emma', 'Number': 104, 'Age': 18},
}

output = open('stu_data.pkl', 'wb')

pickle.dump(stu, output)