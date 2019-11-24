#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/23 0023 15:49
#@Author  :    tb_youth
#@FileName:    mzitu_test.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import requests
import os
from lxml import etree
from projects.spider import  header
import time

# domain : 'https://www.mzitu.com/'
#url = 'https://i5.meizitu.net/thumbs/2019/10/207660_16d06_236.jpg'

class MzituDemo():
    def __init__(self):
        self.headers = {
            'Referer': 'https://www.mzitu.com/xinggan/page/3/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
        }

    def get_type_url(self,url,headers):
        response = requests.get(url,headers=headers)
        # with open('domain.html', 'wb') as f:
        #     f.write(res.content)
        html_ele = etree.HTML(response.text)
        #//ul[@id="menu-nav"]/li/a/@href
        type_url_list = html_ele.xpath('//ul[@id="menu-nav"]/li/a/@href')
        print(type_url_list)
        return type_url_list[1:]

    #得到大分类页中的每组图的url
    def get_group_url(self,type_url,referer):
        self.headers['Referer'] = referer
        response = requests.get(type_url,headers=self.headers)
        # print(response.status_code)
        html_ele = etree.HTML(response.text)

        # //ul[@id="pins"]/li
        # 组url：href，封面:data-original,标题：alt
        group_url_list = html_ele.xpath('//ul[@id="pins"]/li/a/@href')
        # 封面'./a/img/@data-original'

        #<div class="nav-links">
        page_num = html_ele.xpath('//div[@class="nav-links"]/a/text()')[-2]
        page_num = int(page_num)
        # url: type_url + /page/i
        for i in range(2,page_num+1):
            url = '%s/page/%d'%(type_url,i)
            response = requests.get(url,headers=self.headers)
            time.sleep(2)
            html_ele = etree.HTML(response.text)
            group_url_list += html_ele.xpath('//ul[@id="pins"]/li/a/@href')
            break
        # for url in group_url_list:
        #     print(url)
        return group_url_list

    #获取组图url
    def get_group_image_url(self,group_url,referer):
        self.headers['Referer'] = referer
        response = requests.get(group_url, headers=self.headers)
        # print(response.status_code)
        html_ele = etree.HTML(response.text)
        #  <div class="pagenavi">,//div[@class="pagenavi"]
        page_num = html_ele.xpath('//div[@class="pagenavi"]/a/span/text()')[-2]
        digt_num = len(page_num)
        page_num = int(page_num)
        #<div class="main-image"><p><a href="https://www.mzitu.com/207660/2" ><img src="https://i5.meizitu.net/2019/10/16d01.jpg"
        #'//div[@class="main-image"]/p/img/@src'
        group_image_url = html_ele.xpath('//div[@class="main-image"]/p/a/img/@src')[0]

        url,type = group_image_url.rsplit('.',maxsplit=1)
        group_image_base_url = url[:-digt_num]
        # print(group_image_url)
        group_image_url_list = []
        #referer ： Referer: https://www.mzitu.com/207660/i
        for i in range(1,page_num+1):
            group_image_url = '%s%02d.%s'%(group_image_base_url,i,type)
            group_image_url_list.append(group_image_url)
            # print(group_image_url)
        return group_image_url_list

    #下载单张图片
    def download_image(self,url,referer,download_dir='mzi_images'):
        self.headers['Referer'] = referer
        response = requests.get(url,headers=self.headers)
        # print(response.status_code)
        image_name = '%s/%s'%( download_dir,url.split('/')[-1])
        print(image_name, '下载中...')
        with open(image_name,'wb') as f:
            f.write(response.content)
        time.sleep(1)
        print(image_name, '下载完成！')

    #按图片组下载
    def download_image_by_group(self,group_url,referer):
        download_dir = group_url.strip('/').rsplit('/')[-1]
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        group_image_url_list = self.get_group_image_url(group_url,referer)
        # print(group_image_url_list)
        referer = '%s%s'%(referer,download_dir)
        # print(referer)
        print('本图片组编号为:',download_dir)
        for url in group_image_url_list:
            self.download_image(url,referer,download_dir)
        print('-'*50)
    #按类别下载
    def download_image_by_type(self):
        pass

if __name__=='__main__':
    #组图编号：207660
    # url = 'https://i5.meizitu.net/thumbs/2019/10/207660_16d06_236.jpg'
    # url = 'https://i5.meizitu.net/thumbs/2019/10/207505_16a11_236.jpg'
    # referer = 'https://www.mzitu.com/xinggan/page/3/'
    m = MzituDemo()

    download_dir = 'mzi_images'
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
    # text = '''
    # :authority: www.mzitu.com
    # :method: GET
    # :path: /
    # :scheme: https
    # accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    # accept-encoding: gzip, deflate, br
    # accept-language: zh-CN,zh;q=0.9
    # cache-control: max-age=0
    # cookie: Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1574495287; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1574502728
    # referer: https://www.mzitu.com/page/232/
    # upgrade-insecure-requests: 1
    # user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36
    # '''
    # url = 'https://www.mzitu.com/'
    # h = header.Headers()
    # headers = h.get_headers(text)
    # #获取主页顶部图片分类（大分类）
    # m.get_type_url(url,headers)

    # #获取大分类页中个各图片组url
    # url = 'https://www.mzitu.com/xinggan/'
    # referer = 'https://www.mzitu.com/'
    # m.get_group_url(url,referer)

    #获取图片组url
    # url = 'https://www.mzitu.com/207660/'
    url = 'https://www.mzitu.com/212294'
    referer = 'https://www.mzitu.com/xinggan/'
    # m.get_group_image_url(url,referer)
    m.download_image_by_group(url,referer)
    # #下载单张图片
    # m.download_image(url,referer)