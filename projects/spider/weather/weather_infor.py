#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/1/26 0026 22:48
#@Author  :    tb_youth
#@FileName:    weather_infor.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import requests
import json
from projects.spider import header
class Weather:
    def __init__(self,text):
        h = header.Headers()
        self.headers = h.get_headers(text)
        self.data = {
            'source': 'pc',
            'weather_type': 'observe|forecast_1h|forecast_24h|index|alarm|limit|tips|rise',
            'province': '广东',
            'city': '广州',
            'county': '番禺区',
        }
        self.url =  'https://wis.qq.com/weather/common?source=pc&weather_type=observe%7Cforecast_1h%7Cforecast_24h%7Cindex%7Calarm%7Climit%7Ctips%7Crise' \
                    '&province={}&city={}&county={}'.format(self.data['province'],self.data['city'],self.data['county'])
    def get_pre_data(self):
        response = requests.get(self.url,headers=self.headers)
        response.encoding = 'utf-8'
        res = json.loads(response.text)
        # for i in res.items():
        #     print(i)
        with open('./res.txt','w',encoding='utf-8') as f:
            for key,value in res['data'].items():
                line = '{}:{}'.format(key,value)
                f.write(line+'\n')


if __name__=='__main__':
    text = '''
    Referer: https://tianqi.qq.com/index.htm
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36
    '''
    w = Weather(text)
    w.get_pre_data()

