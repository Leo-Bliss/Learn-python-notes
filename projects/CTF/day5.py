#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/30 0030 21:49
#@Author  :    tb_youth
#@FileName:    day5.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import  requests
import re

#web21:秋名山老司机

# url = 'http://123.206.87.240:8002/qiumingshan/'
# cnt = 20
# while cnt:
#     req = requests.session()
#     res = req.get(url)
#     res.encoding = 'utf-8'
#     res = res.text
#     # print(res.text)
#     res = re.findall(r'<div>(.*?)</div>', res, re.S)[0]
#     data = {
#         'value': eval(res[:-3])
#     }
#     res = req.post(url, data=data)
#     res = str(res.text)
#     if(res.find('flag')):
#         print(res)
#         break
#     cnt -= 1

#web22 :速度要快
import base64
url = 'http://123.206.87.240:8002/web6/'
req = requests.session()
headers = req.get(url).headers
flag = headers.get('flag')
flag = base64.b64decode(flag)
flag = base64.b64decode(flag) #要解码两次！！！
flag = re.search('[0-9]+', str(flag))[0]
data = {
    'margin': flag
}
res = req.post(url, data=data)
print(res.text)



