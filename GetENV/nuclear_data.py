from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from CommonFunctions import *
from bs4 import BeautifulSoup
import requests
import re
import os
import pandas as pd
import numpy as np






def save_nuclear_Radiation():
    try:
        get_nuclear_data(url_nuclear)
        l_nuclear_value1= np.reshape(l_nuclear_value,(1,9))
        path_nuclear = r'Data\全国空气吸能数据\核电站\核电站'
        currentTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        save_excel(colnums = l_nuclear_name, data = l_nuclear_value1 , path = path_nuclear ,currentTime = currentTime)
        print('核电站空气吸能' +currentTime + '下载完成')
    except:
        print('空气吸能数据出现错误，无法下载')
