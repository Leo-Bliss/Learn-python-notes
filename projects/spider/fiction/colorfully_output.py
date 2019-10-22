#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/21 0021 16:52
#@Author  :    tb_youth
#@FileName:    colorfully_output.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

from colorama import Fore, Back, Style
#控制台中输出不同颜色字体
for color in ['GREEN', 'RED', 'BLUE', 'YELLOW', 'WHITE']:
    print (getattr(Fore, color), "It's color will be", color)
    print (getattr(Back, color), "It's color will be", color)
    print (Style.RESET_ALL)
