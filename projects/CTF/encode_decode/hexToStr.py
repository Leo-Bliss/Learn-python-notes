#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/5 0005 22:26
#@Author  :    tb_youth
#@FileName:    hexToStr.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import binascii

def inner_hex_to_str(s):
    res = binascii.a2b_hex(s).decode('utf-8')
    print(res)
    return res

def hex_to_str(s):
    #16进制4位一个数，即0xab,每个ox在s中省略了
    res = ''.join([chr(int(s[i:i+2],16)) for i in range(0,len(s),2)])
    print(res)
    return res

if __name__=='__main__':
    s = '666c61677b616537333538376261353662616566357d'
    print(hex_to_str(s)==inner_hex_to_str(s))