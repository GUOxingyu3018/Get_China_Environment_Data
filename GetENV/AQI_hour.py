import requests
from bs4 import BeautifulSoup
from CommonFunctions import *
import pandas as pd
import time
import xlrd
import xlwt
from xlutils.copy  import copy


def get_data(url):
    l_data = []
    l_info = []
    r = requests.get(url)
    html_doc = r.text
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
    currentTime = time.strftime("%Y-%m-%d-%H",time.localtime(time.time()))
    url = 'http://datacenter.mep.gov.cn/aqiweb2/'
    if bool_connect(url) == True:
        try:       
            AQI_hour_data = get_data(url)
            path = r'Data\AQI_Hour_Report.xls'
            wb = xlrd.open_workbook(path)
            newBook = copy(wb)
            sheetName = 'Sheet1'
            sheet = newBook.get_sheet(sheetName)
            for x in AQI_hour_data:
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
                sheet.write(lastRow,9,currentTime)
            newBook.save(path)         
            print(currentTime + 'AQI_Hour_Report is Downloaded')
        except Exception as e:
            print(currentTime+ 'Failed to Dowmload AQI_Hour_Report')
    else:
        print(currentTime+ 'Failed to Dowmload AQI_Hour_Report')

        
   
      