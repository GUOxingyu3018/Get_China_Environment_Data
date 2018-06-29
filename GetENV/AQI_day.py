from bs4 import BeautifulSoup
from CommonFunctions import *
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import pandas as pd
import xlrd
import xlwt
from xlutils.copy  import copy


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
    currentTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    try:
        url = 'http://datacenter.mep.gov.cn/aqiweb2/'
        AQIData = get_data(url)
        path = r'Data\ChinaAQIDailyReport.xls'
        wb = xlrd.open_workbook(path)
        newBook = copy(wb)
        sheetName = 'Sheet1'
        sheet = newBook.get_sheet(sheetName)
        
        for x in AQIData:      
                lastRow = len(sheet.rows)            
                sheet.write(lastRow,0,x[0])
                sheet.write(lastRow,1,x[1])
                sheet.write(lastRow,2,x[2])
                sheet.write(lastRow,3,x[3])
                sheet.write(lastRow,4,currentTime)
        newBook.save(path)          
        print(currentTime + 'ChinaAQIDailyReport is Downloaded')
    except Exception as e:
        print(currentTime + 'ChinaAQIDailyReport Failed to Download'+ e)

