#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/4 0004 19:38
#@Author  :    tb_youth
#@FileName:    strToHex.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

#-------编码——————

import binascii
#调已有模块，字符串转16进制
def inner_str_to_hex(s):
    str_hex = binascii.b2a_hex(s.encode('utf-8'))
    res = b'0x' + str_hex  # type:bytes
    # 转换为str：res.decode('ascii')
    print(res.decode('ascii'))
    return res.decode('ascii')

'''
**自己写脚本**
基本原理:每个元素先转换为ascii值，每个ascii转换为hex，
之后拼接，最后加上'0x'前缀
'''
def str_to_hex(s):
    ss = ''.join([hex(ord(c)).strip('0x') for c in s])
    res = '0x'+ss
    print(res)
    return res


if __name__=='__main__':
    s = 'counter'
    inner_str_to_hex(s)
    print('-'*50)
    str_to_hex(s)

