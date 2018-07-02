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
import xlrd
import xlwt
from xlutils.copy  import copy


value = []
def get_data(url_city):
    chrome_browser = webdriver.Chrome(r"chromedriver.exe")    
    chrome_browser.get(url_city)
    source = BeautifulSoup(chrome_browser.page_source, 'html.parser')
    chrome_browser.close()
    chrome_browser.quit()                          
    #获取监测点的值    
    for n in source.find_all('span', class_ = 'label'):      
        value.append(n.text)

#if __name__ == '__main__': 
def save__Radiation():
    url_city = 'http://data.rmtc.org.cn:8080/gis/listtype0M.html'
    url_nuclear = 'http://data.rmtc.org.cn:8080/gis/listtype1M.html'
    currentTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    try:
        get_data(url_city)
        get_data(url_nuclear)
        path = r'Data\NationalRadiationEnvironmentalData.xls'
        wb = xlrd.open_workbook(path)
        newBook = copy(wb)
        sheetName = 'Sheet1'
        sheet = newBook.get_sheet(sheetName)
        lastRow = len(sheet.rows)
        
        for x in np.array(np.arange(40)):
            sheet.write(lastRow,x,value[x])
        sheet.write(lastRow,40,currentTime)
        newBook.save(path)
        print(currentTime + 'NationalRadiationEnvironmentalData is Downloaded')
    except:
        print(currentTime + 'NationalRadiationEnvironmentalData Failed to Download')
    