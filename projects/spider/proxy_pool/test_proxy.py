#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/24 0024 23:29
#@Author  :    tb_youth
#@FileName:    test_proxy.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import requests
from projects.spider import header
def test_good_proxy(url,headers):
    with open('good_proxies.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            proxy = line.strip('\n')
            proxies = {
                'http':proxy,
                'https':proxy,
            }
            try:
                response = requests.get(url,proxies=proxies,headers=headers,timeout=10)
                print(response.status_code)
                print(response.text)
            except Exception as e:
                print(proxy,'不可用')
                print(e)
                pass




if __name__=='__main__':
    url = 'https://www.liaoxuefeng.com/wiki/1016959663602400/1017629247922688'
    text = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: OUTFOX_SEARCH_USER_ID_NCOO=2036154330.990675; Hm_lvt_2efddd14a5f2b304677462d06fb4f964=1574589106; Hm_lpvt_2efddd14a5f2b304677462d06fb4f964=1574589712
    Host: www.liaoxuefeng.com
    Referer: https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36
    '''
    h = header.Headers()
    headers = h.get_headers(text)
    test_good_proxy(url,headers)
