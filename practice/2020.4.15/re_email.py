# -*- encoding: utf-8 -*-
'''
@File    :   email.py
@Time    :   2020/04/15 09:10:09
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#练习:
#题目1：匹配出163的邮箱地址，且@符号之前有4到20位英文或者数字字符，例如hello@163.com

import re

def main():
    email = input("请输入邮箱地址：")
    ret = re.match(r'[a-zA-Z0-9]{4,20}@163\.com$', email)
    if ret:
        print("输入的邮箱地址有效！%s", ret.group())
    else:
        print("输入的邮箱地址无效！")

if __name__ == '__main__':
    main()