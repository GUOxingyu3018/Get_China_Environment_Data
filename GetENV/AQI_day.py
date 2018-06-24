from bs4 import BeautifulSoup
from CommonFunctions import *
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def get_data(url):
    l_data = []
    l_info = []
    #引入浏览器
    chrome_browser = webdriver.Chrome(r"chromedriver.exe")    
    chrome_browser.get(url)
    #模拟单击AQI日报按钮
    click_btn = chrome_browser.find_element_by_class_name('tab_btn ')
    ActionChains(chrome_browser).click(click_btn)
    #print(chrome_browser.page_source)
    source = BeautifulSoup(chrome_browser.page_source, 'html.parser')
    #数据提取规则
    for n in source.find_all('td'):
        l_info.append(n.text.strip())
    #print(l_info)
    del l_info[:3303]
    #将连续的数据按要求切成多个列表的组合    
    l_data = [l_info[i:i + 4] for i in range(0, len(l_info), 4)]
    chrome_browser.close()
    chrome_browser.quit()
    return l_data
    print(l_data)

if __name__ == '__main__':
#def save_AQI_day():
    url = 'http://datacenter.mep.gov.cn/aqiweb2/'
    if bool_connect(url)  == True:
        data = get_data(url)
        name = name = ['城市', 'AQI', '级别','首要污染物']
        path = r'Data\全国AQI日报\AQI'
        currentTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        save_excel(colnums = name, data = data, path =path, time = currentTime)
        print('AQI日报'+ currentTime + '下载成功')
    else:
        print('AQI日报网站服务不稳定')

#scheduler = BlockingScheduler()
#scheduler.add_job(save_AQI_day, 'interval', hours = 6)
#scheduler.start()