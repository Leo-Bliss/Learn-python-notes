#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/5 0005 14:58
#@Author  :    tb_youth
#@FileName:    day6.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
字符串在内存中以Unicode表示，一个字符对应多个字节
如果要在网络上上传输或者保存到磁盘，就需要把字符串
变为以字节为单位的bytes。
即：'abc' --> b'abc'
转变方式
英文：xxx.encode('ascii')
中文：xxx.encode('utf-8')
'''
import re
import base64
import urllib.parse


with open('1.txt') as f:
    encode_b64 = f.read()

#初始base64编码
print(encode_b64)
print('-'*100)

#base64解码
decode_b64 =  base64.b64decode(encode_b64)
# b'xxx' 此时单位还是bytes
# print(decode_b64)

#转换为字符串，ascii解码即可
decode_b64 = decode_b64.decode('ascii')
print(decode_b64)
print('-'*100)

#0-7的整数,为8进制编码
encode_8 = decode_b64
encode_8 = re.findall(r'\d+', encode_8)
# print(encode_8)
#8进制转换为10进制并且转换为ascii对应的字符,最后连接成字符串
decode_8 = ''.join([chr(int(c,8)) for c in encode_8])
print(decode_8)
print('-'*100)

#\x，现在为16进制编码
encode_16 = decode_8
encode_16 = re.findall(r'\d+', encode_16)
# print(encode_16)
#16进制转换为10进制并且转换为ascii对应的字符,最后连接成字符串
decode_16 = ''.join([chr(int(c,16)) for c in encode_16])
print(decode_16)
print('-'*100)

#&#、&#x、\u 都可以用来表示一串 unicode 编码

#u开头，为unicode编码其中一种形式
encode_unic = decode_16
#提取数据生成列表
encode_unic = re.findall(r'[\d\w]+',encode_unic)
# print(encode_unic)
#再转换为字符串
encode_unic = ''.join([s.replace('u',r'\u') for s in encode_unic])
#\u ,unicode 解码
decode_unic = encode_unic.encode('ascii').decode('unicode-escape')
print(decode_unic)
print('-'*100)

#此时为ascii编码
#提取数据生成列表
encode_ascii = re.findall('\d+', decode_unic)
# print(encode_ascii)
#所有数字转换为ascii对应的字符
decode_ascii = ''.join([chr(int(c)) for c in encode_ascii])
print(decode_ascii)
print('-'*100)

# &#x，此时转换为了另一种unicode编码
encode_unic2 = decode_ascii
#提取数据生成列表
encode_unic2 = re.findall(r'\d+\w?',encode_unic2)
# print(encode_unic2)
#列表16进制转换为10进制，然后根据ascii对应字符，并连接成字符串
decode_unic2 = ''.join([chr(int(c,16)) for c in encode_unic2])
print(decode_unic2)
print('-'*100)

# &#,此时又是unicode的另一种编码形式
encode_unic3 = decode_unic2
#提取数据生成列表
encode_unic3 = re.findall('\d+', encode_unic3)
#根据ascii对应字符，并连接成字符串
decode_unic3 = ''.join([chr(int(c)) for c in encode_unic3])
print(decode_unic3)
print('-'*100)

#此时为url编码
encode_url = decode_unic3
#url解码就可以得到flag~
decode_url = urllib.parse.unquote(encode_url)

flag = decode_url
print(flag)
