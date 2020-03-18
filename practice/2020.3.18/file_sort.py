# -*- encoding: utf-8 -*-
'''
@File    :   file_sort.py
@Time    :   2020/03/18 15:55:18
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

# 练习4:   一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出到另外一个文件中:
#           姓名      学号      分数
#           张三      101         78
#           李四      102         87
#           王五       103        83

f = open(r'E:\Study\Year2_2nd\Python\PythonWorkspace\practice\2020.3.18\student.txt', 'r', encoding = 'UTF8')
f1 = open(r'E:\Study\Year2_2nd\Python\PythonWorkspace\practice\2020.3.18\student_copy.txt', 'w', encoding = 'UTF8')

f_list = f.readlines()
f_list1 = []

for i in f_list:
    f_list1.append(i.strip().split())

f_list1 = f_list1[1: len(f_list1)]
sorted_list = sorted(f_list1, key = lambda x: x[2], reverse = True)

f1.write("排序后：\n")
f1.write("姓名\t学号\t分数\n")
for i in sorted_list:
    f1.write('\t'.join(i))
    f1.write('\n')

f.close()
f1.close()