# -*- encoding: utf-8 -*-
'''
@File    :   8.times_of_str.py
@Time    :   2020/03/10 10:49:21
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#8  请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
#   例如，输入 aaaabbc，输出：a:4

def get_times(s):
    dict_letter = {}
    for i in s:
        if i in dict_letter:
            dict_letter[i] += 1
        else:
            dict_letter[i] = 1
    sorted_dict = sorted(dict_letter.items(), key = lambda x: x[1], reverse = True)
    print(sorted_dict[0])

s = input("请输入字符串：")
get_times(s)
