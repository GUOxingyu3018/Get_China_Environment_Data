from AQI_day import *
from NationalRadiationEnvironmentalData import *
from AQI_hour import *
from AQI_predict import *
from ChinaSurfaceWateInfo import *
import time
from apscheduler.schedulers.blocking import BlockingScheduler

#爬取日报数据
def save_day():    
    save_AQI_day()
    time.sleep(180)
    save__Radiation()
    time.sleep(180)
    save_surfacewater()
    time.sleep(180)        
    save_AQI_predict()
       
#爬取时报
def save_hour():  
    save_AQI_hour()
    time.sleep(180)


if __name__ == '__main__':
    print('开始爬取数据')
    scheduler = BlockingScheduler()
    scheduler.add_job(save_day, 'interval',max_instances = 200, hours = 24) # 循环运行间隔时间   
    time.sleep(100)
    scheduler.add_job(save_hour, 'interval',max_instances = 5,minutes = 60)
    scheduler.start()
    