# -*- encoding: utf-8 -*-
'''
@File    :   10.cal.py
@Time    :   2020/03/10 11:32:58
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#10 编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)

def calculate(m, n, operator):
    if operator ==  '1':
        return m + n
    if operator == '2':
        return m - n
    if operator == '3':
        return m * n
    if operator == '4':
        return m / n

choice = input("请选择运算符(1.+ 2.- 3.* 4./):")
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
result = calculate(num1, num2, choice)
print("运算结果为：", result)