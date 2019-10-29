#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/26 0026 22:55
#@Author  :    tb_youth
#@FileName:    get_bestSellersBooks.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import requests
from projects.spider import header
# import re
from  bs4 import BeautifulSoup

class Book:
    def __init__(self,rk,src,name,star,author,price=None):
        self.rank = rk
        self.img_src = src
        self.name = name
        self.star = star
        self.author = author
        self.price = price

    def print_book_info(self):
        print('排行:',self.rank)
        print('封面:',self.img_src)
        print('书名:%s  链接: %s'%(self.name.get('title'),self.name.get('href')))
        print('书评:%s  推荐度: %s'%(self.star.get('comment_href'),self.star.get('reconmmended_percengtage')))
        print('作者:',self.author)
        print('原价:%s 折后价:%s 电子书价格:%s'%(self.price.get('price_n'),self.price.get('price_r'),self.price.get('price_e')))

class BestSellers:
    def __init__(self,text):
        # 构造请求头
        self.headers = header.Headers().get_headers(text)

    def get_all_data(self,choose='24hours',year='0',month='0'):
        # 构造请求url
        url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-%s-%s-%s-1-"%(choose,year,month)
        url_list = [url + str(i) for i in range(1, 26)]
        for url in url_list:
            page_data = self.get_page_data(url)
            break
        pass

    def get_page_data(self,url):
        response = requests.get(url,self.headers)
        response.encoding = 'gb2312'
        html = response.text
        soup = BeautifulSoup(html,'lxml')# 或使用'html.parser',parser -->语法分析器，分析程式，解析器
        page_data = []
        for p in soup.find_all('ul','bang_list clearfix bang_list_mode'):
            books_info = p.find_all('li')
            # print(books_info)
            for book_info in books_info:
                #排名
                rank = book_info.find('div',class_='list_num').get_text()
                #封面
                img = book_info.find('div',class_='pic').img
                src = img.get('src')
                #书名
                a = book_info.find('div',class_='name').a
                a_href = a.get('href')
                a_title = a.get('title')
                name = {'href':a_href,'title':a_title}
                #推荐度
                star = book_info.find('div',class_='star')
                star_href = star.a.get('href')
                star_rate = star.find('span',class_='tuijian').text
                star = {'comment_href': star_href, 'reconmmended_percengtage': star_rate}
                #作者
                author = book_info.find('div',class_='publisher_info').text
                #价格
                price_n = book_info.find('div',class_='price').find('span',class_='price_n').text #原价
                price_r = book_info.find('div', class_='price').find('span', class_='price_r').text #折后价
                price_e = book_info.find('div', class_='price').find('p', class_='price_e').find('span',class_='price_n') #电子书价格
                price_e = price_e.text if price_e is not None else None
                price = {'price_n':price_n, 'price_r': price_r,'price_e': price_e}
                #单个图书对象
                book = Book(rank,src,name,star,author,price)
                book.print_book_info()
                page_data.append(book)
                print('+---------------------------------------------------------------+')
        return page_data


#当当网top500,每页20条数据，共25页
'''
根据需要，top500分类（对应url）：
近日：
1.近24小时 ：http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-1 
2.近7日： http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-1
3.近30日： http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-1
2019年各月（当年各月份）：
1. 1月： http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-month-2019-1-1-1
2. 2月： http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-month-2019-2-1-1
...
往年：
1. 2015年：http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2015-0-1-1
...
4. 2018年:http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-1

总体：http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-(recent,month,year)-(0,year)-(0,month)-1-(page)
recent的表述有：24hours,rencent7，recent30
要整年数据，month --> 0
只要最近数：year --> 0,month---> 0
'''



if __name__ =='__main__':
    text = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: ddscreen=2; ddscreen=2; from=422-kw-1-%D0%D0%D2%B5%B6%A8%CD%B6-%D6%F7%D5%CB%BB%A7_PC-%B9%D9%CD%F8_m.dangdang.com; order_follow_source=P-422-kw-1%7C%231%7C%23www.baidu.com%252Fbaidu%253Fisource%253Dinfinity%2526iname%253Dbaidu%2526itype%253Dweb%2526tn%253D78040160_34_pg%2526ch%253D5%2526ie%253Dutf-8%2526wd%253D%2525E5%2525BD%7C%230-%7C-; ddscreen=2; __permanent_id=20191026224308883219556102616917937; __visit_id=20191026224308885219503741273709498; __out_refer=1572100989%7C!%7Cwww.baidu.com%7C!%7C%25E5%25BD%2593%25E5%25BD%2593%25E7%25BD%2591; __ddc_1d=1572100989%7C!%7C_utm_sem_id%3D11057663; __ddc_24h=1572100989%7C!%7C_utm_sem_id%3D11057663; __ddc_15d=1572100989%7C!%7C_utm_sem_id%3D11057663; __ddc_15d_f=1572100989%7C!%7C_utm_sem_id%3D11057663; producthistoryid=24198400; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D1%26district_id%3D1110101%26town_id%3D-1; NTKF_T2D_CLIENTID=guest314E213F-26E7-65AA-77FC-088BFC588A5A; nTalk_CACHE_DATA={uid:dd_1000_ISME9754_guest314E213F-26E7-65,tid:1572101422167165}; __rpm=...1572102740347%7C...1572102851495; __trace_id=20191026231412125160984632773737599
    Host: bang.dangdang.com
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36
    """
    # 现在爬取2018年top500
    best = BestSellers(text)
    choose = 'year'
    year = '2018'
    best.get_all_data(choose,year)






