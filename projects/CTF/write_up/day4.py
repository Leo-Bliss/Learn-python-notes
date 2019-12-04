#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/24 0024 10:52
#@Author  :    tb_youth
#@FileName:    day4.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth


#web5
# import  requests
# from  lxml import  etree
# url = 'http://123.206.87.240:8002/web5/'
# response = requests.get(url)
# # with open('web5.html','wb') as f:
# #     f.write(response.content)
#
# html_ele = etree.HTML(response.text)
# print(html_ele.xpath('//div[@style="display:none;"]/text()')[0])
# #console执行："ctf{whatfk}"


#头等舱
#burpsuit抓包，查看响应头

#flag在index里
#查看源代码，发现/index.php?file=show.php
#index.php?file=php://filter/read=convert.base64-encode/resource=index.php
#然后将base64解码

#管理员系统
'''
f12查看源码，发现base64串：dGVzdDEyMw==
解码的到test123，估计为密码，用户名admin

登入：IP禁止访问，请联系本地管理员登陆，IP已被记录.

用burpsuit抓包刚才登入的状态，在headers头加入：X-Forworded-For:127.0.0.1
放行查看response即可

'''


