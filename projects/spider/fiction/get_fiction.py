#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/21 0021 22:15
#@Author  :    tb_youth
#@FileName:    get_fiction.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import math
from projects.spider import header
from zhon import hanzi
# import string

def get_chapter(response):
    html = re.findall(r'<dd>(.*?)</dd>',response,re.S)[0]
    # print(html)
    chapter = re.findall(r'<a target="_blank"(.*?)<',html,re.S)
    #print(chapter)
    chapter_list = []
    for item in chapter:
        href = re.findall(r'href="(.*?)"',item,re.S)[0]
        title = re.findall(r'title="(.*?)"',item,re.S)[0]
        #print(title+':'+href)
        chapter_list.append({title:href})
    return chapter_list
# #alignment
# #居中对齐
# def center(text,max_len=30):
#     num = (max_len - len(text))//2
#     if num:
#         add_chars = ' ' * num
#         text = '%s%s%s'%(add_chars,text,add_chars)
#     print(text)

def format_write(title,content,max_len=30):
    head = title.split('&#13;')
    #print(head)
    #标题居中对齐
    f = open('demo.doc','w',encoding='utf-8')
    title = head[0]
    #print(title.center(max_len))
    f.write(title.center(max_len))
    f.write('\n')
    #本章节字数
    text_num = int(re.findall(r'\d+',head[1])[0])
    #计算预计阅读时间
    read_time = math.ceil(text_num/400)
    tip = '本章预计阅读时间:%d分钟'%read_time
    #print(tip.center(max_len))
    f.write(tip.center(max_len))
    f.write('\n')
    #中文标点符号
    hpunc = hanzi.punctuation
    # #英文标点符号
    # punc = string.punctuation
    for item in content:
        item = '  '+item
        cnt = 0
        i = 0
        while i < (len(item)):
            if(cnt%max_len!=max_len-1 and i!=len(item)-1):
                #print(item[i],end='')
                f.write(item[i])
                cnt += 1
            else:
                #print(item[i],end='')
                f.write(item[i])
                #使每行非标点符号开头
                if(i+1<len(item) and item[i+1] in hpunc):
                    #print(item[i+1],end='')
                    f.write(item[i+1])
                    i += 1
                #print('')
                f.write('\n')
                cnt = 0
            i += 1
    print(title,'下载完成！')
    f.close()


def download_chapter(chapter_list,headers):
    domain = 'https://www.17k.com'
    for chapter in chapter_list:
        for title,href in chapter.items():
            url = '%s%s'%(domain,href)
            #print(url)
            chapter_html = requests.get(url,headers)
            chapter_html.encoding = 'utf-8'
            chapter_html = chapter_html.text
            #print(chapter_html)
            chapter_content = re.findall(r'<div class="p">(.*?)<p></p>',chapter_html,re.S)[0]
            chapter_content = re.findall('<p>(.*?)</p>',chapter_content,re.S)
            # print(title)
            # for item in chapter_content:
            #     print(item)
            format_write(title,chapter_content)
        break




if __name__ == '__main__':
    text = """
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9
    cache-control: max-age=0
    cookie: GUID=f6597cb6-25cd-43d5-96c8-eb2ea99dfa4d; UM_distinctid=16cddcec2482d7-04aeefb6e74675-37c143e-144000-16cddcec2494d4; OUTFOX_SEARCH_USER_ID_NCOO=818054790.6546456; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22f6597cb6-25cd-43d5-96c8-eb2ea99dfa4d%22%2C%22%24device_id%22%3A%2216cddcec123373-0c4abeac302c3-37c143e-1327104-16cddcec124238%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; CNZZDATA5647345=cnzz_eid%3D1744002380-1567087340-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1571621102; Hm_lvt_9793f42b498361373512340937deb2a0=1571624102; Hm_lpvt_9793f42b498361373512340937deb2a0=1571624124
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36 
    """
    headers = header.Headers().get_headers(text)
    url = 'https://www.17k.com/list/3039605.html'
    response = requests.get(url,headers)
    response.encoding = 'utf-8'
    response = response.text
    # print(response)
    lst = get_chapter(response)
    download_chapter(lst,headers)
