#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/8 0008 13:56
#@Author  :    tb_youth
#@FileName:    CommonHelper.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
用于装载qss文件
'''
class CommonHelper():
    @staticmethod
    def readQSS(style):
        with open(style,'r',encoding='utf-8')as f:
            return  f.read()
