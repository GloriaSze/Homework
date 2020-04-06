# -*- encoding: utf-8 -*-
'''
@File    :   3.encryption.py
@Time    :   2020/04/06 16:43:06
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
#       Tom   admin   XXXXX
#       Jack  root    XXXXX   

import hashlib

dict = {}
md5 = hashlib.md5()

with open('account.txt', 'w') as file:
    file.write('姓名\t账号\t密码\n')
    for i in range(5):
        name = input("请输入第{0}个同学的姓名：".format(i + 1))
        account = input("请输入第{0}个同学的账号：".format(i + 1))
        password = input("请输入第{0}个同学的密码：".format(i + 1))
        md5.update(password.encode('utf-8'))
        file.write(name + '\t' + account + '\t' + md5.hexdigest() + '\n')