# -*- encoding: utf-8 -*-
'''
@File    :   1.write.py
@Time    :   2020/03/20 15:27:25
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；

def input_kb():
    try:
        while 1:
            i = input()
            if i != ' ':
                input_list.append(i)
            else:
                return input_list
    except IOError as err:
        print('IOError:{0}'.format(err))

def write_txt(list):
    with open(r'E:\Study\Year2_2nd\Python\PythonWorkspace\homework3\input.txt', 'w') as file:
        for i in list:
            file.write(i)
            file.write('\n')

input_list = []
print("请输入信息(以空格行结束)：")
input_kb()
print(input_list)
write_txt(input_list)
