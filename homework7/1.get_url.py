# -*- encoding: utf-8 -*-
'''
@File    :   1.get_url.py
@Time    :   2020/04/22 17:03:20
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
#   提示，文件有1000行，注意控制每次读取的行数；

import re

def main():
    url_list = []
    with open('webspiderUrl.txt', 'r', encoding = 'UTF8') as file:
        line = file.readlines()
        for i in line:
            url_list.append(re.findall('http://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', i))
    with open('url_result.txt', 'w') as file:
        for i in url_list:
            file.write("\n".join(i) + '\n')
            
if __name__ == "__main__":
    main()