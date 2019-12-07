#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/7 0007 13:47
#@Author  :    tb_youth
#@FileName:    md5_.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
python md5加密
'''
import hashlib

def encode(s):
    md5 = hashlib.md5()
    md5.update(s.encode(encoding='utf-8'))
    md5_encode = md5.hexdigest()
    return md5_encode

if __name__== '__main__':
    s = 'password'
    print(encode(s))

