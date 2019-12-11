#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/11 0011 19:30
#@Author  :    tb_youth
#@FileName:    plot_basis2.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
绘制折线图
'''

import matplotlib.pyplot as plt

data1 = [2211,2323,1560,7788,3322,1000,7089]
data2 = [1235,3456,666,8886,2323,3000,223]
#中文乱码处理
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = [str(i)+'h' for i in range(1,len(data1)+1)]

plt.plot(x,data1,marker='*',mec='r',label='股票1')
plt.plot(x,data2,marker='o',mec='b',lw=2,label='股票2')

#label显示
plt.legend()

#x轴标签
plt.xticks(x)

plt.title('股票价格波动')

plt.ylim(100,10000)

#标上数值
for x,y in enumerate(data1):
    plt.text(x,y+100,'%s'%y,ha='center')

for x,y in enumerate(data2):
    plt.text(x,y+500,'%s'%y,ha='center')

# #图的保存，一定要放在show之前
# plt.savefig(r'./images/polyLine.png')
#保存为矢量图
plt.savefig(r'./images/example1.svg',dpi=600,format='svg')
plt.show()

