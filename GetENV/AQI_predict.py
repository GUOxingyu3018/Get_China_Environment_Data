from bs4 import BeautifulSoup
from CommonFunctions import *
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import pandas as pd
import xlrd
import xlwt
from xlutils.copy  import copy
import numpy as np


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

def save_AQI_predict():
#if __name__ == '__main__':
    currentTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    url = 'http://106.37.208.228:8082/'
    try:      
        if bool_connect(url) == True:
            AQI_predict_report_data = get_data(url)
            data_24 = AQI_predict_report_data[0]
            data_48 = AQI_predict_report_data[1]
            data_72 = AQI_predict_report_data[2]

            
            path = r'Data\AQI_predict_report.xls'
            wb = xlrd.open_workbook(path)
            newBook = copy(wb)
            sheetName = 'Sheet1'
            sheet = newBook.get_sheet(sheetName)
            for x in np.array(np.arange(42)):
                lastRow = len(sheet.rows)
                sheet.write(lastRow,0,data_24[x])
                sheet.write(lastRow,1,data_48[x])
                sheet.write(lastRow,2,data_72[x])
                sheet.write(lastRow,3,currentTime)
            newBook.save(path)         
            print(currentTime + 'AQI_predict_report is Downloaded')         
        else:
            print('AQI预报网站服务不稳定')
    except Exception as e:        
        print(e)

