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
    #浏览器的位置
    chrome_browser = webdriver.Chrome(r"chromedriver.exe")    
    chrome_browser.get(url)
    #模拟单击页表按钮
    time.sleep(5)
    click_btn = chrome_browser.find_element_by_link_text('列表').click()
    #ActionChains(chrome_browser).click(click_btn)
    #print(chrome_browser.page_source)
    source = BeautifulSoup(chrome_browser.page_source, 'html.parser')    
    #数据提取规则
    for n in source.find_all('p'):       
       l_info.append(n.text.strip())
    #print(l_info)    
    chrome_browser.close()
    chrome_browser.quit()
    del l_info[:25]
    l_data = [l_info[i:i + 46] for i in range(0, len(l_info), 46)]  
    return l_data

#def save_AQI_predict():
if __name__ == '__main__':
    try:
        url = 'http://106.37.208.228:8082/'
        if bool_connect(url) == True:
            data = get_data(url)
            path = r'Data\全国AQI预报24-48-72\AQI预报'
            currentTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
            save_excel(data = data, path= path, time = currentTime)
            print('AQI预报' + currentTime + '下载完成')
        else:
            print('AQI预报网站服务不稳定')
    except Exception as e:        
        print(e)

#scheduler = BlockingScheduler()
#scheduler.add_job(save_AQI_predict, 'interval', hours = 12)
#scheduler.start()


