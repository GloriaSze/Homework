# -*- encoding: utf-8 -*-
'''
@File    :   3.identification.py
@Time    :   2020/04/10 15:52:59
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#3  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）

std_account = 'fzs'
std_password = 'SxyFzs999'

def identity(func):
    def wrapper(*args, **kwargs):
        account = input("请输入用户账号：")
        password = input("请输入账号密码；")
        if account == std_account and password == std_password:
            print("登陆成功！")
            func(*args, **kwargs)
        else:
            print("登录失败")
    return wrapper

@identity
def func1():
    print("这是第一个测试函数！")

@identity
def func2():
    print("这是第二个测试函数！")

@identity
def func3():
    print("这是第三个测试函数！")

choice = int(input("请输入想要运行的函数（1. func1 2. func2 3. func3）："))
if choice == 1:
    func1()
elif choice == 2:
    func2()
elif choice == 3:
    func3()
else:
    print("请输入数字（1-3）！")