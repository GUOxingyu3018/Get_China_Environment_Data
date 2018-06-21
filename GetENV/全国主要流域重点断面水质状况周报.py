from apscheduler.schedulers.blocking import BlockingScheduler
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from datetime import datetime
from CommonFunctions import *
from bs4 import BeautifulSoup
from ghost import *
import requests
import re
import os
import pandas as pd
import numpy as np
import urllib

l_info = []
l_data = []
def get_data(url):    
    chrome_browser = webdriver.Chrome(r"chromedriver.exe")    
    chrome_browser.get(url)
    #print(chrome_browser.page_source)
    source = BeautifulSoup(chrome_browser.page_source, 'html.parser')
    #html_doc = requests.get(url).text
    #source = BeautifulSoup(html_doc, 'html.parser')
    #for n in source.find_all('tr'):
        #l_info.append(n.text)         
        #print(l_info)
        
if __name__ == '__main__':
    url = 'http://datacenter.mep.gov.cn/websjzx/report!list.vm?xmlname=1512553411227&roleType=CFCD2084&permission=null'
    get_data(url)
    path = r'Data\全国主要流域重点断面水质状况表\全国主要流域重点断面水质状况表'
    currentTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    
    data = l_info
    #save_excel(data = data,path = path, currentTime = currentTime)
    
    
