# -*- encoding: utf-8 -*-
'''
@File    :   6.similarity.py
@Time    :   2020/03/27 10:02:48
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#6  在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 请读取文章内容,进行词频的统计;
#   并分别输出统计结果到另外的文件存放;
#   比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);

import json

def words_count(path):
    sentences_list = []
    words_list = []
    words_dict = {}
    try:
        with open(path, 'r') as f:
            for i in f.readlines():
               sentences_list.append(i.strip())
        for i in sentences_list:
            words_list = i.split()
            for i in words_list:
                if i in words_dict:
                    words_dict[i] += 1
                else:
                    words_dict[i] = 1
        return words_dict
    except FileNotFoundError as err:
        print('FileNotFoundError:{0}'.format(err))

def compare(list1, list2):
    count = 0
    for i in list1:
        for j in list2:
            if i[0] == j[0]:
                count += 10
    return count

path1 = r'E:\Study\Year2_2nd\Python\PythonWorkspace\homework3\essay1.txt'
path2 = r'E:\Study\Year2_2nd\Python\PythonWorkspace\homework3\essay2.txt'
dict1 = words_count(path1)
dict2 = words_count(path2)
list1 = sorted(dict1.items(), key = lambda x: x[1], reverse = True)[0:10]
list2 = sorted(dict2.items(), key = lambda x: x[1], reverse = True)[0:10]

json_info1 = json.dumps(dict1)
json_info2 = json.dumps(dict2)
with open(r'E:\Study\Year2_2nd\Python\PythonWorkspace\homework3\result.txt', 'w') as file:
    file.write('essay1: ')
    file.write(json_info1)
    file.write('\n')
    file.write('essay2: ')
    file.write(json_info2)

print('两篇文章的相似度为：{0}%'.format(compare(list1, list2)))