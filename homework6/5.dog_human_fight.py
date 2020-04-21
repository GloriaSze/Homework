# -*- encoding: utf-8 -*-
'''
@File    :   5.dog.py
@Time    :   2020/04/21 14:29:52
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#五  请写一个小游戏，人狗大站;  规则:
#    1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
#        人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
#    2   人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
#        人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
#    3   对战规则: 
#     A  随机决定,谁先开始攻击; 
#     B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
#     C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;

import random
import time

class Dog():
    def __init__(self, name, strength, hp):
        self.name = name
        self.strength = strength
        self.hp = hp

    def attack(self, human):
        human.hp -= self.strength
        if human.strength - 2 <= 0:
            human.strength = 0
        else:
            human.strength -= 2
        #time.sleep(1)
        print("{0}被{1}攻击了，失去血量{2}，剩余血量{3}，当前攻击力为{4}".format(human.name, self.name, self.strength, human.hp, human.strength))

class Human():
    def __init__(self, name, strength, hp):
        self.name = name
        self.strength = strength
        self.hp = hp

    def attack(self, dog):
        dog.hp -= self.strength
        if dog.strength - 3 <= 0:
            dog.strength = 0
        else:
            dog.strength -= 3
        #time.sleep(1)
        print("{0}被{1}攻击了，失去血量{2}，剩余血量{3}，当前攻击力为{4}".format(dog.name, self.name, self.strength, dog.hp, dog.strength))

def fight():
    pass

def main():
    human1 = Human('张三', 10, 100)
    human2 = Human('李四', 10, 100)
    dog1 = Dog('旺财', 15, 80)
    dog2 = Dog('发财', 15, 80)
    dog3 = Dog('汪汪', 15, 80)
    human_list = []
    human_list.append(human1)
    human_list.append(human2)
    dog_list = []
    dog_list.append(dog1)
    dog_list.append(dog2)
    dog_list.append(dog3)

    print("人狗大战开始！")

    while True:
        choice = random.randint(0, 1)
        dog = random.sample(dog_list, 1)
        human = random.sample(human_list, 1)

        if choice == 0:
            dog[0].attack(human[0])
        else:
            human[0].attack(dog[0])

        for i in dog_list:
            if i.hp <= 0 or i.strength == 0:
                dog_list.remove(i)
        
        for i in human_list:
            if i.hp <= 0 or i.strength == 0:
                human_list.remove(i)
        
        if len(human_list) == 0:
            print("狗取得胜利！")
            break
        if len(dog_list) == 0:
            print("人取得胜利！")
            break

if __name__ == '__main__':
    main()