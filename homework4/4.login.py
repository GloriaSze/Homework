# -*- encoding: utf-8 -*-
'''
@File    :   4.login.py
@Time    :   2020/04/06 17:17:36
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#4  (继续上面的练习) 模拟用户登录:
#   5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   
#   系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);

import hashlib

list = []
list_name = []
md5 = hashlib.md5()

with open('account.txt', 'r') as file:
    name = input("请输入登录同学的姓名：")
    for i in file.readlines():
        list.append(i.strip().split())
    for i in list:
        list_name.append(i[0])
    if name in list_name:
        index = list_name.index(name)
        account = input("请输入账号：")
        if account is list[index][1]:
            password = input("请输入密码：")
            md5.update(password.encode('utf-8'))
            if md5.hexdigest() == list[index][2]:
                print("登录成功！")
            else:
                print("密码错误！登录失败！")
        else:
                print("账号错误！")
    else:
        print("姓名错误！")