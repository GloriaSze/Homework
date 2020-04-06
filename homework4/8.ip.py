# -*- encoding: utf-8 -*-
'''
@File    :   8.ip.py
@Time    :   2020/04/06 20:46:37
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#8 京东二面笔试题
#1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
#2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip

import random

ip_dict = {}

with open('ips.txt', 'w') as file:
    for i in range(1200):
        file.write('172.25.254.' + str(random.randint(0, 255)) + '\n')

with open('ips.txt', 'r') as file:
    for i in file:
        i = i.strip()
        if i in ip_dict:
            ip_dict[i] += 1
        else:
            ip_dict[i] = 1
sorted_list = sorted(ip_dict.items(), key = lambda x: x[1], reverse = True)
print(sorted_list[:10])