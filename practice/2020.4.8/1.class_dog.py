# -*- encoding: utf-8 -*-
'''
@File    :   1.class_dog.py
@Time    :   2020/04/08 09:13:28
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#练习:  
#定义一个dog类(颜色, 名称), 里面有一个狗叫的方法; 不同的狗叫声可能不一样;  然后实例化几条狗, 然后统计实例化狗的数量

class Dog():
    count = 0
    color = ''
    name = ''

    def __init__(self, c, n):
        self.color = c
        self.name = n
        Dog.count += 1

    def dog_bark(self):
        print("{0}在叫".format(self.name))

    @staticmethod
    def print_amount():
        print("狗的数量为:{0}".format(Dog.count))
    
chaiquan = Dog('yellow', 'chaiquan')
chaiquan.dog_bark()
keji = Dog('white', 'keji')
keji.dog_bark()
Dog.print_amount()