#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/23 0023 22:25
#@Author  :    tb_youth
#@FileName:    get_arrival_flights.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import requests
import re
import time
from openpyxl import workbook
last_item = []
#处理时间
def get_time(s1,s2):
    tmp = s2[4:6] + s2[7:9]
    time = s1.replace('-', '') + tmp
    return time

#数据项处理：完全清洗每一条数据
def get_data(s):
    s = str(s)
    #id = re.findall(r'id="(.*?)"',s,re.S)[0]
    data_flightNo = re.findall(r"data-flightNo='(.*?)'",s)
    #print(data_flightNo)
    airport_terminal = re.findall(r'<li class="column w80">(.*?)</li>',s)[1]
    #print(airport_terminal)
    detail = re.findall(r'>(.*?)</p>',s)
    #['航班号','机型','出发地/经停点','航站楼','计划抵达时间','实际抵达时间']
    item = [0 for x in range(6)]
    item[0] = data_flightNo[0]
    item[1] = detail[9].replace('\t','')
    item[2] = detail[6]
    item[3] = airport_terminal
    item[4] = get_time(detail[1],detail[2])
    item[5] = get_time(detail[4],detail[5])
    #print(item)
    return item
    #wa.append(item)
    #print(data_flightNo,airport_terminal,detail)

#数据预处理：初步清洗整页数据
def get_pre_data(response):
    html = response.text
    aim_list = re.findall(r'<div class="row" (.*?)data-totalPage=""></div>', html, re.S)
    #print(aim_list)
    n = len(aim_list)
    print('本页数据共%d条'%n)
    global aim_date
    #按官网预计抵达时间存储
    for e in aim_list:
        item_tmp = get_data(e)
        if item_tmp[4][0:4]=='20190912':
            wa.append(item_tmp)
        print(item_tmp)
    global last_item
    if(n != 0):
        last_item = get_data(aim_list[n-1])
    else:
        last_item = []

#加载第1页数据
def load():
    heads = {
        'Cookie': '___rl__test__cookies=1568344114712; JSESSIONID=43496DA383A0768578DF19CD59612C74; \
        ___rl__test__cookies=1568343602949; cookieFlag=show; OUTFOX_SEARCH_USER_ID_NCOO=1161335801.\
        1987514; _locale=zh_CN; Hm_lvt_0effb2f651854e064f7d24a159e08bd5=1568340756,1568342071;\
         Hm_lvt_783519365e6df848bd882229527a15bc=1568340756,1568342071; \
         insert_cookie=67313298; Hm_lpvt_0effb2f651854e064f7d24a159e08bd5=1568360222; \
         Hm_lpvt_783519365e6df848bd882229527a15bc=1568360222; CURR_TERMINAL=ALL',
        'Host': 'www.baiyunairport.com',
        'Referer': 'http://www.baiyunairport.com/byairport-web/flight/list?depOrArr=2&type=1&day=0&terminal=ALL',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Mobile Safari/537.36'
    }
    data ={
        'terminal': 'ALL',
        'type': 1,
        'depOrArr': 2,
        'day': -1
    }
    url = 'http://www.baiyunairport.com/byairport-web/flight/list?terminal=ALL&type=1&depOrArr=2&day=-1'
    response = requests.post(url,data,heads)
    response.encoding = 'utf-8'
    get_pre_data(response)
#加载其他页数据
def load_more(flight_no,aim_time):
    url = 'http://www.baiyunairport.com/byairport-web/flight/loadMore'
    heads ={
               'Accept': 'text / html, * / *;q = 0.01',
                'Content - Type': 'application / x - www - form - urlencoded;charset = UTF - 8',
                'Origin': 'http: // www.baiyunairport.com',
                'Referer': 'http: // www.baiyunairport.com / \
                byairport - web / flight / list?depOrArr = 2 & type = 1 & terminal = ALL & day = -1',
                'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
                'X - Requested - With': 'XMLHttpRequest'
    }
    data = {
        'depOrArr': 2,
        'type': 1,
        'day': -1,
        'terminal': 'ALL',
        'flightNo': '%s'%flight_no,
        'dataTime': '%s'%aim_time
    }
    response = requests.post(url,data,heads)
    response.encoding = 'utf-8'
    #print(response.status_code)
    get_pre_data(response)



if __name__ == '__main__':
     #创建表格，用于存储目标数据
     wb = workbook.Workbook()
     wa = wb.active
     #表头
     wa.append(['航班号','机型','出发地/经停点','航站楼','计划抵达时间','实际抵达时间'])
     #爬取第一页数据
     load()
     cnt = 1
     print('---------第%d页数据爬取完成！！----------------'%cnt)
     #print(last_item)
     # 加载更多:爬取第其他页数据
     while len(last_item) != 0:
         flight_no = last_item[0]
         if (last_item[4][0:8]=='20190913'):
             break
         aim_time = last_item[4][0:4]+'-'+last_item[4][4:6]+'-'+last_item[4][6:8]+' '+last_item[4][8:10]\
         +':'+last_item[4][10:12]
         load_more(flight_no,aim_time)
         cnt += 1
         print('---------第%d页数据爬取完成！！----------------' %cnt)
         time.sleep(5)
     #保存数据
     wb.save('20190912_arrival_flight.xlsx')
     print('爬取完成!！！^--^ ')


