# -*- encoding: utf-8 -*-
'''
@File    :   2.student_class.py
@Time    :   2020/04/14 16:16:55
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#二 定义一个学生Student类。有下面的类属性：
#1 姓名 name
#2 年龄 age
#3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
#类方法：
#1 获取学生的姓名：get_name() 返回类型:str
#2 获取学生的年龄：get_age() 返回类型:int
#3 返回3门科目中最高的分数。get_course() 返回类型:int
#写好类以后，可以定义2个同学测试下:

class Student():
    name = ''
    age = None
    score_Chinese = None
    score_Math = None
    score_English = None

    def __init__(self, n, a, c, m, e):
        self.name = n
        self.age = a
        self.score_Chinese = c
        self.score_Math = m
        self.score_English = e

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.score_Chinese, self.score_Math, self.score_English)

fzs = Student('fzs', 18, 95, 90, 80)
sxy = Student('sxy', 20, 100, 90, 100)
print(fzs.get_name(), fzs.get_age(), fzs.get_course())
print(sxy.get_name(), sxy.get_age(), sxy.get_course())