# -*- encoding: utf-8 -*-
'''
@File    :   3.score.py
@Time    :   2020/03/26 20:00:21
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出

try:
    score_list = []
    with open(r'E:\Study\Year2_2nd\Python\PythonWorkspace\homework3\score.txt', 'r', encoding = 'UTF8') as file:
        for i in file:
            score_list.append(i.strip().split())
    
    unsorted_list = score_list[1:len(score_list)]
    sorted_list = sorted(unsorted_list, key = lambda x: int(x[2]), reverse = True)

    print('学号\t姓名\tPython课程分数')
    for i in sorted_list:
        print('\t'.join(i))
except FileNotFoundError as err:
    print('Error:{0}'.format(err))