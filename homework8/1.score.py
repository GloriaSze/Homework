# -*- encoding: utf-8 -*-
'''
@File    :   1.score.py
@Time    :   2020/04/26 21:19:00
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#1  有100个同学的分数：数据请用随机函数生成；
#     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#     B 利用线程池来实现；

import random
import threading
from concurrent.futures import ThreadPoolExecutor

def print_score(list):
    for i in list:
        print(i, end = ' ')

def main():
    score_list = []
    for i in range(100):
        score_list.append(random.randint(0, 100))
    print("利用多线程：")
    for i in range(5):
        t = threading.Thread(target = print_score, args = (score_list[i * 20: (i + 1) * 20],))
        t.start()
    print('\n' + "利用线程池：")
    with ThreadPoolExecutor(max_workers = 5) as pool:
        for i in range(5):
            list = score_list[i * 20: (i + 1) * 20]
            t1 = pool.submit(print_score, list)
    
if __name__ == "__main__":
    main()