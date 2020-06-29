# -*- encoding: utf-8 -*-
'''
@File    :   salary.py
@Time    :   2020/06/23 21:36:19
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

#在51job网站上，爬取2020年发布的Python开发工程师的职位的薪酬，计算北京地区改职位的平均薪酬；
import urllib.request
import re
from concurrent.futures import ThreadPoolExecutor

def get_html(page):
    #获取单页原码

    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{0}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=".format(page)
    #设置请求头
    headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    #创建一个opener
    opener = urllib.request.build_opener()
    #将headers添加到opener中
    opener.addheaders = [headers]
    #将opener安装为全局
    urllib.request.install_opener(opener)
    #用urlopen打开网页
    html = urllib.request.urlopen(url).read().decode('gbk')
    return html

def get_info(html):
    #获取信息

    reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)" href="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? ',re.S)#基本信息
    info = re.findall(reg,html)
    return info

def crawler(page):
    #循环爬取

    salary = []          #存放北京地区薪资

    for i in range(page, page + 10):
        print("正在爬取第"+str(i)+"页数据...")
        html = get_html(i)      
        info = get_info(html)       
        for j in info:
            #print(j)
            with open ('51job.txt','a',encoding='utf-8') as f:
                f.write(j[0]+'\t'+j[1]+'\t'+j[3]+'\t'+j[4]+'\n')
                f.close()
            if "北京" in j[1]:
                salary.append(j[4])
    
    #for i in salary:
    #    print(i)

    print("爬取完毕！")

    return salary

def run_thread_pool(target, args, max_work_count = 3):
    #使用线程池得到返回值

    with ThreadPoolExecutor(max_workers = max_work_count) as t:
        res = t.map(target, args)
        return res

def cal(list):
    #对薪资进行处理

    low = []               #最低薪资
    high = []              #最高薪资
    for i in list:
        pattern = re.compile(r'\d+\.?\d*')
        num = pattern.findall(i)
        if '月' in i:           #月薪
            if '万' in i:
                low.append(float(num[0]) * 10000)
                high.append(float(num[1]) * 10000)
            if '千' in i:
                low.append(float(num[0]) * 1000)
                high.append(float(num[1]) * 1000)
        if '年' in i:           #年薪转换为月薪，默认以万为单位
            low.append((float(num[0]) * 10000) / 12)
            high.append((float(num[1]) * 10000) / 12)
        if '日' in i:           #日薪转换为月薪，默认为30天/月，将其当做最低工资
            low.append(float(num[0]) * 30)

    salary_lowest = sum(low) / len(low)
    salary_highest = sum(high) / len(high)

    print("北京地区的平均薪资为：%d - %d/月" %(salary_lowest, salary_highest))

def main():
    salary_bj = []             #将爬取的北京薪资存在一个列表里
    res = run_thread_pool(target = crawler, args = (1, 11, 21))
    for i in res:
        for j in i:
            salary_bj.append(j)
    
    cal(salary_bj)           

if __name__ == '__main__':
    main()
