# -*- encoding: utf-8 -*-
'''
@File    :   2.website.py
@Time    :   2020/04/29 14:40:19
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；

import requests
import threading

def getHtmlText(list):
    try:        # 网络连接有风险，异常处理很重要
        for url in listL:
            print(url)
            r = requests.get(url,timeout=30)    # 查一下这个方法的使用
            r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
            r.encoding = r.apparent_encoding
            if r.text:
                print("可正常访问")
    except:
         print("访问产生异常")

def main():
    with open("url_data.txt", 'r') as file:
        lines = file.readlines()
        for i in range(5):
            t = threading.Thread(target = getHtmlText, args = (lines[i * 10: (i + 1)* 10],))
            t.start()

if __name__ == '__main__':
    main()