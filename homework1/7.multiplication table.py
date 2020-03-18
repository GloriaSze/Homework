# -*- encoding: utf-8 -*-
'''
@File    :   multiplication table.py
@Time    :   2020/03/06 19:16:48
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#7 打印输出9*9乘法表，按照下面的格式：

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}'.format(j, i, i*j), end = ' ')
    print("\n")