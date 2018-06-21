from apscheduler.schedulers.blocking import BlockingScheduler
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from datetime import datetime
from CommonFunctions import *
from bs4 import BeautifulSoup
import requests
import re
import os
import pandas as pd
import numpy as np


l_city_name = []
l_city_value = [] 
l_city_value1 = []
url_city = 'http://data.rmtc.org.cn:8080/gis/listtype0M.html'

l_nuclear_name = []
l_nuclear_value = []
l_nuclear_value1 = []
url_nuclear = 'http://data.rmtc.org.cn:8080/gis/listtype1M.html'

def get_city_data(url):
#if __name__ == '__main__': 
    #html_doc = requests.get(url).text
    chrome_browser = webdriver.Chrome(r"chromedriver.exe")    
    chrome_browser.get(url_city)
    #print(chrome_browser.page_source)
    source = BeautifulSoup(chrome_browser.page_source, 'html.parser')
    chrome_browser.close()
    chrome_browser.quit()
    #获取监测点的名称    
    for n in source.find_all('div', class_ = 'divname'):
        name = n.text.strip()
        l_city_name.append(name)#shape(1,31)                            
    #获取监测点的值    
    for n in source.find_all('span', class_ = 'label'):      
        l_city_value.append(n.text)#shape(31,1)     

def get_nuclear_data(url):
#if __name__ == '__main__':
    #html_doc = requests.get(url).text
    chrome_browser = webdriver.Chrome(r"chromedriver.exe")    
    chrome_browser.get(url_nuclear)
    #click_btn = chrome_browser.find_element_by_partial_link_text('核电厂监测点')
    #ActionChains(chrome_browser).click(click_btn)
    #print(chrome_browser.page_source)
    source = BeautifulSoup(chrome_browser.page_source, 'html.parser')
    chrome_browser.close()
    for n in source.find_all('div', class_ = 'divname'):
        name = n.text.strip()
        l_nuclear_name.append(name)
    for n in source.find_all('span', class_ = 'label'):  
        l_nuclear_value.append(n.text)

#if __name__ == '__main__': 
def save_nuclear_Radiation():
    try:
        get_nuclear_data(url_nuclear)
        del l_nuclear_name[9:]
        del l_nuclear_value[9:]
        l_nuclear_value1= np.reshape(l_nuclear_value,(1,9))
        path_nuclear = r'Data\全国空气吸能数据\核电站\核电站'
        currentTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        save_excel(colnums = l_nuclear_name, data = l_nuclear_value1 , path = path_nuclear ,time = currentTime)
        print('核电站空气吸能' +currentTime + '下载完成')
    except Exception as e:
        print(e)


           

def save_city_Radiation():
#if __name__ == '__main__':      
    try:              
        get_city_data(url_city)
        del l_city_name[31:]
        del l_city_value[31:]
        l_city_value1 = np.reshape(l_city_value,(1,31))# 行列转置，shape（1，31）      
        path_city = r'Data\全国空气吸能数据\省会\省会'        
        currentTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        save_excel(colnums = l_city_name, data = l_city_value1, path = path_city ,currentTime = currentTime)       
        print('省会空气吸能' +currentTime + '下载完成')
    except Exception as e :
        print(e)


#scheduler = BlockingScheduler()
#scheduler.add_job(save_Radiation, 'interval', minutes = 2)
#scheduler.start()
        