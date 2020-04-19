# -*- encoding: utf-8 -*-
'''
@File    :   1.dog_trade.py
@Time    :   2020/04/14 16:00:47
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#一、定义一个狗类,里面有一个列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
#   实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;

class Dog():
    dog_list = [
        {
            'name': 'chaiquan',
            'color': 'yellow', 
            'amount': 3,
            'price': 1000
        },
        {
            'name': 'keji',
            'color': 'white',
            'amount': 4,
            'price': 1500
        },
        {
            'name': 'bianmu',
            'color': 'black',
            'amount': 2,
            'price': 2000
        }
    ]

    @classmethod
    def trade(cls, name, num):
        total = 0
        if name == 1:
            cls.dog_list[0]['amount'] -= num
            total += cls.dog_list[0]['price'] * num
            print("您需要支付{0}元".format(total))
        if name == 2:
            cls.dog_list[1]['amount'] -= num
            total += cls.dog_list[1]['price'] * num
            print("您需要支付{0}元".format(total))
        if name == 3:
            cls.dog_list[2]['amount'] -= num
            total += cls.dog_list[2]['price'] * num
            print("您需要支付{0}元".format(total))

    @classmethod
    def print_info(cls):
        for i in cls.dog_list:
            print(i['name'] + '\t' + str(i['amount']) + '只')

while True:
    name = int(input("请输入您想要购买的狗的种类（1.柴犬 2.柯基 3.边牧）："))
    amount = int(input("请输入想要购买的数量："))
    Dog.trade(name, amount)
    choice = input("还要继续购买吗？y/n")
    if choice != 'y':
        Dog.print_info()
        break