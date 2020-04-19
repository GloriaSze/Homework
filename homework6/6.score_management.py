# -*- encoding: utf-8 -*-
'''
@File    :   6.score_management.py
@Time    :   2020/04/19 20:32:17
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#六  用面向对象,实现一个学生Python成绩管理系统;
#    学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#    实现对学生信息及成绩的增,删,改,查方法;

class Student():
    stu_class = ''
    number = ''
    name = ''
    score = ''

    def __init__(self, c, num, n, s):
        self.stu_class = c
        self.number = num
        self.name = n
        self.score = s

    def add(self):
        with open('student.txt', 'a', encoding = 'UTF8') as file:
            file.write(self.stu_class + '\t\t' + self.number + '\t\t' + self.name + '\t\t' + self.score + '\n')
        print("学生信息已添加！")

    def delete(self):
        content = []
        with open('student.txt', 'r+', encoding = 'UTF8') as file:
            for line in file.readlines():
                content.append(line.strip().split())
            for i in content:
                if self.name in i:
                    content.remove(i)
            print(content)
            file.seek(0)
            file.truncate()
            for i in content:
                file.write('\t\t'.join(i) + '\n')
        print("学生信息已删除！")
    
    def update(self):
        content = []
        with open('student.txt', 'r+', encoding = 'UTF8') as file:
            for line in file.readlines():
                content.append(line.strip().split())
            for i in content:
                if self.name in i:
                    i[0] = self.stu_class
                    i[1] = self.number
                    i[3] = self.score
            file.seek(0)
            file.truncate()
            for i in content:
                file.write('\t\t'.join(i) + '\n')
        print("学生信息已修改！")

    def search(self):
        content = []
        with open('student.txt', 'r+', encoding = 'UTF8') as file:
            for line in file.readlines():
                content.append(line.strip().split())
            for i in content:
                if self.name in i:
                    print("该生的班级为{0}，学号为{1}，Python成绩为：{2}".format(i[0], i[1], i[3]))


def main():
    with open('student.txt', 'w', encoding = 'UTF8') as file:
            file.write('班级\t\t学号\t\t姓名\t\tPython成绩\n')
    
    while True:
        choice = int(input("请输入您需要进行的操作（1.添加学生信息 2.删除学生信息 3.更改学生信息 4.查找学生信息）："))

        if choice == 1:
            stu_class = input("请输入学生班级：")
            num = input("请输入学生学号：")
            name = input("请输入学生姓名：")
            score = input("请输入学生Python成绩：")
            stu = Student(stu_class, num, name, score)
            stu.add()
        elif choice == 2:
            name = input("请输入学生姓名：")
            stu = Student(None, None, name, None)
            stu.delete()
        elif choice == 3:
            name = input("请输入要修改的学生姓名：")
            stu_class = input("请输入修改后的学生班级：")
            num = input("请输入修改后的学生学号：")
            score = input("请输入修改后的学生成绩：")
            stu = Student(stu_class, num, name, score)
            stu.update()
        elif choice == 4:
            name = input("请输入学生姓名：")
            stu = Student(None, None, name, None)
            stu.search()
        else:
            print("输入有误！")
        
        flag = input("继续吗？Y/N")
        if flag == 'N':
            break

if __name__ == '__main__':
    main()