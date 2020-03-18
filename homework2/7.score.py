# -*- encoding: utf-8 -*-
'''
@File    :   7.score.py
@Time    :   2020/03/10 10:40:23
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#7  随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
#   A---成绩>=90;  
#   B-->成绩在 [80,90)
#   C-->成绩在 [70,80)
#   D-->成绩<70

import random

def level(s):
    if s >= 90:
        return("A")
    elif s >=80 and s < 90:
        return("B")
    elif s >= 70 and s < 80:
        return("C")
    else:
        return("D")

for i in range(1, 21):
    s = random.randint(0, 100)
    print('学生：%d, 成绩：%d，等级：%s' %(i, s, level(s)))