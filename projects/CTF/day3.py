#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/23 0023 10:04
#@Author  :    tb_youth
#@FileName:    day3.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth


#点击一百万次
# import requests
# url = 'http://123.206.87.240:9001/test/'
# data = {'clicks':100000000}
# response = requests.post(url,data)
# response = response.text
# print(response)
#之后查找flag即可

#变量1
#("/^\w+$/"):a-z,A-Z,_，0-9,i是不区分大小写
#构造：args=GLOBALS即可