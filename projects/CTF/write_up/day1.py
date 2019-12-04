#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/17 0017 23:26
#@Author  :    tb_youth
#@FileName:    day1.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

#problem_source： https://ctf.bugku.com

import requests
'''
ctf : web
'''

#1

# f12:
# 底下search：flag即可

#2

# f12,修改maxlength=100（要大于答案位数即可）

#3
# url = 'http://123.206.87.240:8002/get/?what=flag'
# print(requests.get(url).text)

#4
# url = 'http://123.206.87.240:8002/post/'
# data = {
#     'what':'flag'
# }
# response = requests.post(url,data=data)
# print(response.text)


# url = 'http://123.206.87.240:8002/get/index1.php?num=TRUE'
# response = requests.get(url)
# print(response.text)

#5
# url = 'http://123.206.87.240:8002/get/index1.php?num=1%20' #1*1
# print(requests.get(url).text)

#6
#直接f12查看（不能点）
#再unicode解码

#7
#修改本机host文件，添加进去，访问。。。baidu

#8 wireshake（用kali自带的） 抓包，搜flag



