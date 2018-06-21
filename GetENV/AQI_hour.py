import requests
from bs4 import BeautifulSoup
from CommonFunctions import *
import pandas as pd
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def get_data(url):
    l_data = []
    l_info = []
    html_doc = requests.get(url).text
    source = BeautifulSoup(html_doc, 'html.parser')
    #数据提取规则
    #获取全部表格的文本，去除空格符后组成列表
    for n in source.find_all('td' ):       
        l_info.append(n.text.strip())

    #将连续的数据按要求切成多个列表的组合    
    l_data = [l_info[i:i + 9] for i in range(0, len(l_info), 9)]

    #循环滚动列表，爬取时会重复抓取数据，删除重复数据
    del l_data[367:]
    return l_data

#存储数据
def save_AQI_hour():
#if __name__ == '__main__':
    url = 'http://datacenter.mep.gov.cn/aqiweb2/' #网站连接不稳定
    currentTime = time.strftime("%Y-%m-%d-%H",time.localtime(time.time()))
    name = ['城市','AQI','PM2.5','PM10','SO2','NO2','CO','O3','首要污染物']     
    path = r'Data\全国AQI时报\AQI时报'
    data = get_data(url)
    if bool_connect(url) ==True:
        save_excel(colnums = name,data = data,path = path, currentTime = currentTime)
        print('AQI时报'+ currentTime + '下载完成')
    else:
        print("AQI日报网站服务不稳定")

#爬取数据间隔时间设置
#scheduler = BlockingScheduler()
#scheduler.add_job(save_AQI_hour, 'interval', hours = 1) # 循环运行间隔时间
#scheduler.start()
    