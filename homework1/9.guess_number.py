# -*- encoding: utf-8 -*-
'''
@File    :   guess_number.py
@Time    :   2020/03/06 20:50:38
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#9 设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；

import random

number = random.randint(1, 100)                 #随机生成数
count = int(input("请输入可猜测的次数："))        #猜测的次数

print(number)

def is_number(n):
    if n < number:
        print("您猜的数字小了！")
        return False
    if n > number:
        print("您猜的数字大了！")
        return False
    if n == number:
        print("恭喜您，猜对了！")
        return True

for i in range(count):
    n = int(input("请输入您猜的数字(1-100)："))
    if is_number(n):
        break
    print("您还有", count-1-i, "次机会")
    if i == 4:
        print("猜测失败！")
        break