#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/23 0023 22:40
#@Author  :    tb_youth
#@FileName:    proxy_1.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import requests
from lxml import etree
from projects.spider import header
import time
from multiprocessing import Pool
import  re

class ProxyDemo(object):
    def __init__(self,url,headers,page_num=1):
        self.page_num = page_num
        self.url,self.headers= url,headers
        self.good_proxy_list = []

    def get_all_proxy(self):
        assert(0)

    def validate_proxy(self,proxy):
        url = 'http://www.baidu.com'
        proxies = {
            'http': proxy,
            'https': proxy,
        }
        try:
            requests.get(url, proxies=proxies, timeout=10)
            print('Good proxy!!!', proxies)
            return proxy
        except Exception as e:
            print(e)
            print('Bad proxy...', proxies)
            return None

    def validate_proxy_by_mulitprocess(self):
        #1.生成进程池
        pool  = Pool(5)
        #将任务设置进入进程池
        #for  task in task_list:
        #    pool.apply_async(func=)
        res_list = []
        for proxy in self.get_all_proxy():
            res = pool.apply_async(func=self.validate_proxy,args=(proxy,))
            res_list.append(res)

        #获取返回值
        good_proxy_list = []
        for res in res_list:
            good_proxy = res.get()
            if good_proxy:
                self.good_proxy_list.append(good_proxy)
        #进程池关闭
        pool.close()
        #等待所有进程结束
        pool.join()

    def save_good_proxy(self):
        with open('good_proxies.txt','a+',encoding='utf-8') as f:
            for proxy in self.good_proxy_list:
                f.write(proxy+'\n')
        print('新写入 %d 个 good proxy...'%len(self.good_proxy_list))


class XiciProxy(ProxyDemo):
    def __init__(self,url,headers,page_num=1):
        super(XiciProxy,self).__init__(url,headers,page_num)

    def get_all_proxy(self):
        url_list = ['%s%d' % (self.url, i) for i in range(1, self.page_num + 1)]
        for url in url_list:
            print(url)
            response = requests.get(url, headers=self.headers)
            html_ele = etree.HTML(response.text)
            # print(response.text)
            # <table id="ip_list">
            #    <tr class="odd">
            proxy_info_list = html_ele.xpath('//table[@id="ip_list"]/tr[@class="odd"]')

            for proxy_info in proxy_info_list:
                ip = proxy_info.xpath('./td[2]/text()')[0]
                port = proxy_info.xpath('./td[3]/text()')[0]
                proxy = '{0}:{1}'.format(ip, port)
                print(proxy)
                yield proxy
            print('-' * 50)
            time.sleep(2)


class FastProxy(ProxyDemo):
    def __init__(self, url, headers, page_num=1):
        super(FastProxy, self).__init__(url, headers, page_num)

    def get_all_proxy(self):
        url_list = ['%s/%d' % (self.url, i) for i in range(1, self.page_num + 1)]
        for url in url_list:
            print(url)
            response = requests.get(url, headers=self.headers)
            # print(response.status_code)
            # with open('fast.html', 'wb') as f:
            #     f.write(response.content)
            '''
            <td data-title="IP">182.92.113.183</td>
            <td data-title="PORT">8118</td>
            '''
            response = response.text
            ip_list = re.findall('<td data-title="IP">(.*?)</td>', response, re.S)
            port_list = re.findall('<td data-title="PORT">(.*?)</td>', response, re.S)
            for ip, port in zip(ip_list, port_list):
                print(ip, port)
                proxy = '{0}:{1}'.format(ip,port)
                yield  proxy
        print('-'*50)


if __name__=='__main__':
    # url = 'https://www.xicidaili.com/nn/'
    # text = '''
    # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    # Accept-Encoding: gzip, deflate, br
    # Accept-Language: zh-CN,zh;q=0.9
    # Cache-Control: max-age=0
    # Connection: keep-alive
    # Cookie: _free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTc5M2Y2ODYzM2U2MDY1M2Y2ZTIwY2NlNDY4ZWI4N2EyBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMU4rRDBIQjlLVzZwaGZlZVdhK2tYQ1NXYnVJSkprK0FxaHNjZ2t2YUVwL3c9BjsARg%3D%3D--6e1a1c64abd8bcf860bd51b65aa8591e7f51ae9e; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1574485419; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1574485419
    # Host: www.xicidaili.com
    # Upgrade-Insecure-Requests: 1
    # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36
    # '''

    url = 'https://www.kuaidaili.com/free/inha'
    text = '''
        accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-CN,zh;q=0.9
        Cache-Control: max-age=0
        Connection: keep-alive
        Cookie: channelid=0; sid=1574524639120836; _ga=GA1.2.1329451401.1574524764; _gid=GA1.2.1298279956.1574524764; _gat=1; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1574524764; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1574524767
        Host: www.kuaidaili.com
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36
        '''
    start = time.time()
    #------------------------------
    h = header.Headers()
    headers = h.get_headers(text)
    # -----------------------------
    # xici_proxy = XiciProxy(url,headers)
    # xici_proxy.validate_proxy_by_mulitprocess()
    # xici_proxy.save_good_proxy()
    #----------------------------
    fast_proxy = FastProxy(url,headers)
    fast_proxy.validate_proxy_by_mulitprocess()
    fast_proxy.save_good_proxy()
    #-----------------------------
    end = time.time()
    print('总耗时：',end-start)

    # for proxy in demo.get_all_proxy():
    #     demo.validate_proxy(proxy)

