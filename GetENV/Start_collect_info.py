from AQI_day import *
from NationalRadiationEnvironmentalData import *
from AQI_hour import *
from AQI_predict import *
from ChinaSurfaceWateInfo import *
import 江苏省空气质量与水质环境
import time
import os


#爬取日报数据
def save():    
    save__Radiation()
    time.sleep(100)
    save_surfacewater()
    time.sleep(100)    
    save_js_AQI()
    time.sleep(100)    
    save_AQI_predict()
    time.sleep(100)
    save_AQI_day()
    time.sleep(200)

#爬取时报
def save_hour():  
    save_AQI_hour()
    time.sleep(2000)


if __name__ == '__main__':   
    print('开始爬取数据')
#爬取数据间隔时间设置
    scheduler = BlockingScheduler()
    scheduler.add_job(save, 'interval',max_instances = 20, hours = 24) # 循环运行间隔时间   
    time.sleep(10000)
    scheduler.add_job(save_hour, 'interval',max_instances = 10,minutes = 60)
    scheduler.start()





