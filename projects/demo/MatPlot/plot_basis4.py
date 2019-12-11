#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/11 0011 21:07
#@Author  :    tb_youth
#@FileName:    plot_basis4.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
绘制散点图
'''

import matplotlib.pyplot as plt
import numpy as np

#数据
n = 50
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)

#计算颜色值
color = np.arctan2(y,x)

#绘制散点图
plt.scatter(x,y,s=60,c=color,marker='o',alpha=0.5)
#设置坐标范围
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))

#显示坐标的值
plt.xticks([-1,0,1,2,3,4])
plt.yticks([-1,0,1,2,3,4])

plt.xlabel('x',fontsize=14)
plt.ylabel('y',fontsize=14)


#防止中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#标题
plt.title('散点图',ha='center')

plt.show()