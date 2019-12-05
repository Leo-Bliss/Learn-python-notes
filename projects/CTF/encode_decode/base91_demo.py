#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/5 0005 21:22
#@Author  :    tb_youth
#@FileName:    base91_demo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import base91
s = '@iH<,{bdR2H;i6*Tm,Wx2izpx2!'
print(base91.decode(s).decode('ascii'))