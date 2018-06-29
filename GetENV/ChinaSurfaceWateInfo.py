from bs4 import BeautifulSoup
from CommonFunctions import *
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import xlrd
import xlwt
from xlutils.copy  import copy




def get_data(url):
    l_data = []
    l_info = []
    chrome_browser = webdriver.Chrome(r"chromedriver.exe")    
    chrome_browser.get(url)
    source = BeautifulSoup(chrome_browser.page_source, 'html.parser')
    #数据提取规则
    for n in source.find_all('td' ):       
       l_info.append(n.text.strip())
    #print(l_info)

    #依据数据的属性个数进行分割长度调整，06/24/2018 添加属性 总有机碳
    l_data = [l_info[i:i + 10] for i in range(0, len(l_info), 10)]

    chrome_browser.close()
    chrome_browser.quit()
    #删除因循环滚动造成的重复爬取的数据
    del l_data[100:]
    #删除表头
    del l_data[0]
    return l_data   
    

def save_surfacewater ():
#if __name__ == '__main__':
    currentTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    try:
        url = 'http://123.127.175.45:8082/'   
        surfaceWaterData = get_data(url)

        path = r'Data\ChinaSurfaceWateInfo.xls'
        wb = xlrd.open_workbook(path)
        newBook = copy(wb)
        sheetName = 'Sheet1'
        sheet = newBook.get_sheet(sheetName)
        #保存数据
        for x in surfaceWaterData:      
            lastRow = len(sheet.rows)
            sheet.write(lastRow,0,x[0])
            sheet.write(lastRow,1,x[1])
            sheet.write(lastRow,2,x[2])
            sheet.write(lastRow,3,x[3])
            sheet.write(lastRow,4,x[4])
            sheet.write(lastRow,5,x[5])
            sheet.write(lastRow,6,x[6])
            sheet.write(lastRow,7,x[7])
            sheet.write(lastRow,8,x[8])
            sheet.write(lastRow,9,x[9])        
        newBook.save(path)         
        print(currentTime + 'ChinaSurfaceWateInfo is Downloaded')
    except Exception as e:
        print(currentTime+ 'Failed to Dowmload ChinaSurfaceWateInfo' + e)



