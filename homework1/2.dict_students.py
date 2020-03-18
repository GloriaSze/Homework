# -*- encoding: utf-8 -*-
'''
@File    :   dict.py
@Time    :   2020/03/06 15:54:28
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#2 一个字典中，存放了10个学生的学号（key）和分数（value）；请筛选输出，大于80分的同学（按照格式：学号：分数）；

score = {
    '1200': 100,
    '1201': 80,
    '1202': 86,
    '1203': 75,
    '1204': 70,
    '1205': 96,
    '1206': 87,
    '1207': 67,
    '1208': 100,
    '1209': 83
}

print("大于80分的同学：")
for key, value in score.items():
    if value > 80:
        print("学号", key ,":", value, "分")