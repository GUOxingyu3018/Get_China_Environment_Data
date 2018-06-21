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
    chrome_browser = webdriver.Chrome(r"chromedriver.exe")    
    chrome_browser.get(url)
    #print(chrome_browser.page_source)
    source = BeautifulSoup(chrome_browser.page_source, 'html.parser')
    #数据提取规则
    for n in source.find_all('td' ):       
       l_info.append(n.text.strip())
    l_data = [l_info[i:i + 9] for i in range(0, len(l_info), 9)]
    chrome_browser.close()
    chrome_browser.quit()
    del l_data[100:]
    return l_data   

def save_surfacewater ():
#if __name__ == '__main__':
    url = 'http://123.127.175.45:8082/'   
    if bool_connect(url) == True: 
        data = get_data(url)
        path = r'Data\国家地表水水质自动监测数据\地表水水质'
        currentTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        save_excel( data = data, path = path, currentTime = currentTime)
        print('地表水水质' + currentTime + '下载完成')
    else:
        print("地表水水质网络连接出错")

#scheduler = BlockingScheduler()
#scheduler.add_job(save_surfacewater, 'interval', hours = 12)
#scheduler.start()


