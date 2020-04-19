# -*- encoding: utf-8 -*-
'''
@File    :   4.student_info.py
@Time    :   2020/04/14 16:56:56
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
#    封装方法，求单个学生的总分，平均分，以及打印学生的信息。

class Student():
    def __init__(self, n, a, g, e, m, c):
        self.name = n
        self.age = a
        self.gender = g
        self.score_English = e
        self.score_Math = m
        self.score_Chinese = c
    
    def total_score(self):
        return self.score_English + self.score_Math + self.score_Chinese
    
    def average_score(self):
        total = self.score_English + self.score_Math + self.score_Chinese
        return total / 3
    
    def print_info(self):
        print("学生姓名为：{0}".format(self.name))
        print("学生年龄为：{0}".format(self.age))
        print("学生性别为：{0}".format(self.gender))
        print("学生各科成绩为（英语，数学，语文）：{0}，{1}，{2}".format(self.score_English, self.score_Math, self.score_Chinese))
    
fzs = Student('fzs', 18, 'male', 90, 85, 81)
fzs.print_info()
print("学生总分为{0}".format(fzs.total_score()))
print("学生平均分为{0}".format(fzs.average_score()))