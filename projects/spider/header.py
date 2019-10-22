#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/21 0021 22:16
#@Author  :    tb_youth
#@FileName:    header.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
import re
class Headers:
    def __init__(self):
       pass
    def get_headers(self,text):
        headers = re.findall(r'(.*):(.*)',text)
        # for key,value in headers:
        #     print(key.strip()+':'+value.strip())
        headers = dict((key.strip(),value.strip()) for key,value in headers)
        return headers


if __name__ == '__main__':
    text = '''
    :authority: www.nowcoder.com
    :method: GET
    :path: /
    :scheme: https
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9
    cache-control: max-age=0
    cookie: NOWCODERUID=104ADABD662C02D4726B73D01FBAB11A; NOWCODERCLINETID=B597D9B8D59B649FE2990BF841B9751B; OUTFOX_SEARCH_USER_ID_NCOO=83387210.41601476; gr_user_id=c3c272b5-0e9a-41fa-83f4-4c731e9563c6; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=727193393; grwng_uid=6c97efae-771e-406b-ac28-431f39c6b072; t=77450E9CDC8FB9F7B9C276D1D4DB66C9; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1570368691,1571395114,1571395806,1571409451; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1571409451; c196c3667d214851b11233f5c17f99d5_gr_session_id=fbfb8789-3d0f-4c76-8e2c-8174fd3f113e; c196c3667d214851b11233f5c17f99d5_gr_last_sent_sid_with_cs1=fbfb8789-3d0f-4c76-8e2c-8174fd3f113e; c196c3667d214851b11233f5c17f99d5_gr_cs1=727193393; c196c3667d214851b11233f5c17f99d5_gr_session_id_fbfb8789-3d0f-4c76-8e2c-8174fd3f113e=true; SERVERID=547d00d82311952605c62ceac64f21fd|1571409454|1571409448
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36
    '''
    h = Headers()
    headers = h.get_headers(text)
    #print(headers)
    url = 'https://www.nowcoder.com/recommendation/user?token=&page=1&pageSize=5&_=1571413707313'
    response = requests.get(url,headers).text
    #print(response)
    #json将字符串解析为字典
    response = json.loads(response)
    print(response)

