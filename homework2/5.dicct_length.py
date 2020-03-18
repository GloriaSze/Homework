# -*- encoding: utf-8 -*-
'''
@File    :   5.dicct_length.py
@Time    :   2020/03/09 17:50:59
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#5  写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;

def renew(dict):
    new_dict = {}
    for k, v in dict.items():
        if len(v) > 2:
            new_dict[k] = v[0: 2]
        else:
            new_dict[k] = v
    return new_dict

dict = {
    'Alice': [1],
    'Bob': [1, 2, 3, 4],
    'Cathy': [1, 2, 3],
    'Daisy': [1, 2]
}
print("新的字典为：", renew(dict))