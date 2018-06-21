#coding:utf-8   
from CommonFunctions import *
import time
import pandas as pd
from datetime import datetime
import numpy as np
import chardet
import urllib3


AQI_num = []
AQI = []
def get_AQI_data(url):    
    html_doc = str(requests.get(url).text.encode("utf-8")) 
    #print(html_doc)
    l_ = html_doc.split('{')
    #print(l_)
    del l_[:2]
    for i in l_:
        n = i[6]+i[7]
        AQI_num.append(n)

c = []
c_name = []
c_publish_level_current = []
c_publish_level_previous = []
def get_water_data(url):
    http  = urllib3.PoolManager()
    html = http.request('GET',url)
    html_doc = html.data.decode('utf-8')

    data = html_doc.split('{')
    
    del data[:2]
    #print(data)
    
    
    for rows in data:
        row = rows.split(',')
        for r in row:
            c.append(r)
    #print(len(c))  =1847
    #获取水质监测点名称
    num_name = 3
    name_num = []
    while num_name < 1847:
        name_num.append(num_name)
        num_name += 8
    c_names = ([c[x] for x in name_num])
    for name in c_names:
        n = name.split(':')[1]
        c_name.append(n)
    #print(c_name)
    
    #获取水质类型
    num_level_current = 5
    water_num = []
    while num_level_current < 1847:
        water_num.append(num_level_current)
        num_level_current += 8
    water_level = ([c[x] for x in water_num])
    #print(water)
    for level in water_level:
        n = level.split(':')[1]
        #print(n)
        c_publish_level_current.append(n)
    #print(c_publish_level_current)    

    

    

#def save_js_AQI():
if __name__ == '__main__':
    url_AQI = 'http://218.94.78.75:20001/sjzx/services/%E6%9F%A5%E8%AF%A2%E7%A9%BA%E6%B0%94%E8%B4%A8%E9%87%8F%E6%97%A5%E6%8A%A5.ashx'
    get_AQI_data(url_AQI)
    path_AQI = r'Data\江苏省空气和水质数据\AQI日报\AQI'
    currentTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    name_0 = ['南京市迈皋桥','南京市草场门','南京市山西路','南京市中华门','南京市瑞金路',
            '南京市玄武湖','南京市浦口','南京市仙林大学城','南京市奥体中心','无锡市雪浪',
            '无锡市黄巷','无锡市曹张','无锡市漆塘','无锡市东亭','无锡市旺庄',
            '无锡市荣巷','无锡市堰桥','徐州市黄河新村','徐州市淮塔','徐州市新城区',
            '徐州市桃园路','徐州市农科院','徐州市鼓楼区政府','徐州市铜山区招生办','常州市市监测站',
            '常州市武进监测站','常州市安家','常州市行政中心','常州市经开区','常州市钟楼',
            '苏州市上方山','苏州市南门','苏州市彩香','苏州市轧钢厂','苏州市吴中区',
            '苏州市苏州新区','苏州市苏州工业园区','苏州市相城区','南通市南郊','南通市虹桥','南通市城中',
            '南通市星湖花园','南通市紫琅学院','连云港市市环境监测站','连云港市德源药业',
            '连云港市胡沟管理处','连云港市矿山设计院','淮安市钵池山','淮安市北京南路',
            '淮安市市监测站','淮安市楚州区监测站','淮安市淮阴区监测站','盐城市盐城电厂',
            '盐城市市监测站','盐城市开发区管委会','盐城市宝龙广场','扬州市城东财政所',
            '扬州市市监测站','扬州市邗江监测站','扬州市五台山医院',
            '镇江市职教中心','镇江市丹徒区监测站','镇江市市疾控中心','泰州市公园路',
            '泰州市莲花','泰州市留学生创业园','泰州市王营','宿迁市宿迁学院','宿迁市宿迁中学',
            '宿迁市宿豫区环保局','宿迁市市供电局']
    #'镇江市新区办事处'
    dic = {}
    index = 0
    #print(len(name_0))
    #print(len(AQI_num))
    while index < 71:
        dic[name_0[index]] = AQI_num[index]
        AQI.append(dic)
        index += 1
    data = []
    name = []
    for v in AQI[0].values():
        data.append(v)

    for k in AQI[0].keys():
        name.append(k)
    #print(np.shape(name))
    save_excel(colnums =name, data = np.reshape( data,(1,71)), path= path_AQI, time = currentTime)
    print('江苏省空气质量日报' +currentTime + '下载完成')

    url_water = "http://218.94.78.75:20001/sjzx/services/%E6%9F%A5%E8%AF%A2%E6%B0%B4%E8%B4%A8%E8%87%AA%E5%8A%A8%E7%9B%91%E6%B5%8B%E5%91%A8%E6%8A%A5.ashx"
    get_water_data(url_water)
    path_water  = r'Data\江苏省空气和水质数据\水质日报\水质日报'
    #c_n = np.reshape(c_name,(1,231))
    c_p = np.reshape(c_publish_level_current,(1,231))
    save_excel(colnums=c_name,data= c_p,path= path_water,time= currentTime )
    print('江苏省水质数据日报' +currentTime + '下载完成')