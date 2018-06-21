import requests
import time
import csv
import os
import pandas as pd

#判断网页是否可以打开,返回200，表示可以打开
def bool_connect(url):
    try:
        response = requests.get(url).status_code          
        if response == 200:
            return True
        else:
            return False
    except:
        return False

#数据保存
def save_excel(colnums=None, data = None , path = None , time = None ):
    '''
    colnums:保存数据的名称
    data：保存的数据
    path：保存的路径
    currentTime：保存的时间属性
    '''
    save = pd.DataFrame(columns = colnums, data = data)
    save.to_excel(path +time + '.xlsx' )
