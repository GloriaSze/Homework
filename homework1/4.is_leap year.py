# -*- encoding: utf-8 -*-
'''
@File    :   is_leap year.py
@Time    :   2020/03/06 16:32:09
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#4  判断用户输入的年份是否为闰年

year = int(input("请输入年份："))
if(year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(year, "年是闰年")
else:
    print(year, "年不是闰年")