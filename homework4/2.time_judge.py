# -*- encoding: utf-8 -*-
'''
@File    :   2.time_judge.py
@Time    :   2020/03/31 20:53:26
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  
# 将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；

import datetime

def judge(date):
    result = date.isocalendar()
    print("当前日期是{0}年的第{1}周，周{2}".format(result[0], result[1], result[2]))

def school(date):
    school_date = str(date.year) + '/2/17'
    calendar_date = datetime.datetime.strptime(school_date, '%Y/%m/%d')
    difference = (date - calendar_date).days
    week = difference // 7
    print("当前日期是当年校历的第{0}周，周{1}".format(week + 1, date.isocalendar()[2]))


date_input = input("请输入一个日期（以年/月/日的格式)：")
date = datetime.datetime.strptime(date_input, '%Y/%m/%d')
judge(date)
school(date)