#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/11 0011 22:08
#@Author  :    tb_youth
#@FileName:    plot_basis7.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
绘制气泡图:
气泡图用也是scatter方法绘制和散点图一样。
差别在于点的大小不一样，散点图的点都是一样的，
而气泡图点的大小不一样。
'''

import pandas as pd
import matplotlib.pyplot as plt
#中文乱码处理
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

d = {
    '时间':pd.Series([i for i in range(2006,2011)]),
     '数量':pd.Series([10,200,120,150,300]),
    '大小':pd.Series([50,130,40,50,160]),
    '分类':pd.Series([1,2,0,1,2]),
    '判断':pd.Series([True,True,True,True,True]),
}
df = pd.DataFrame(d)

size = df['大小'].rank()
print(size)
n = 20
color = {0:'red',1:'blue',2:'orange'}
plt.scatter(df['数量'],df['大小'],color=[color[i] for i in df['分类']],s=size*n,alpha=0.6)
plt.xlabel('数量')
plt.ylabel('大小')
plt.show()

