# -*- encoding: utf-8 -*-
'''
@File    :   employee.py
@Time    :   2020/03/06 19:30:35
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#8 设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；  
#  将这10个员工，按照工资从高到低打印输出；


employees = {}
employees['01'] = {'name': 'Gloria', 'year': 1, 'salary': 6000}
employees['02'] = {'name': 'Feng', 'year': 2, 'salary': 10000}
employees['03'] = {'name': 'Lee', 'year': 2, 'salary': 9000}
employees['04'] = {'name': 'Sze', 'year': 1, 'salary': 5500}
employees['05'] = {'name': 'Zhang', 'year': 3, 'salary': 15000}
employees['06'] = {'name': 'Zhao', 'year': 2, 'salary': 7000}
employees['07'] = {'name': 'Qian', 'year': 4, 'salary': 20000}
employees['08'] = {'name': 'Sun', 'year': 1, 'salary': 6500}
employees['09'] = {'name': 'Zhou', 'year': 3, 'salary': 9500}
employees['10'] = {'name': 'Wu', 'year': 5, 'salary': 30000}
print("工号    ", "姓名         ", "工龄       ", "工资        ")

sortedlist = sorted(employees.items(), key = lambda e: e[1]['salary'], reverse = True)
for i in sortedlist:
    print(i)