# -*- encoding: utf-8 -*-
'''
@File    :   count.py
@Time    :   2020/04/03 08:41:10
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

def createCounter():
    i = 0
    def acc():
        nonlocal i
        i += 1
        return i
    return acc

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
