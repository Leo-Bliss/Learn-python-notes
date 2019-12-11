#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/11 0011 18:44
#@Author  :    tb_youth
#@FileName:    plot_basis1.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
绘制柱状图
'''

import matplotlib.pyplot as plt
'''
#构建数据
sales = [455,885,234,669,888,789,1315]

#中文乱码处理
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#绘图
plt.bar(range(len(sales)),sales,0.4,color='r',alpha=0.8)

#添加标签
plt.ylabel('销量')
#添加标题
plt.title('水果11月销量')
#添加刻度标签
plt.xticks(range(len(sales)),['苹果','香蕉','梨','葡萄','芒果','菠萝','西瓜'])
#设置y轴的刻度
plt.ylim([100,1500])
#为每个条形添加数值
for x,y in enumerate(sales):
    plt.text(x,y+50,'%s'%y,ha='center')
plt.show()


#水平条形图 ：barh

#绘图
plt.barh(range(len(sales)),sales,0.4,color='r',alpha=0.8)

#添加标签
plt.xlabel('销量')
#添加标题
plt.title('水果11月销量')
#添加刻度标签
plt.yticks(range(len(sales)),['苹果','香蕉','梨','葡萄','芒果','菠萝','西瓜'])
#设置y轴的刻度
plt.xlim([100,1500])
#为每个条形添加数值
for x,y in enumerate(sales):
    plt.text(y+50,x,'%s'%y,ha='center')
plt.show()
'''
#柱状图和折线图混合使用

sales = [455,885,234,669,999,789,1315]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#绘制折线
#构建折线图数据
jan_sales = [123,567,345,987,888,567,233]
x = ['苹果','香蕉','梨','葡萄','芒果','菠萝','西瓜']
plt.plot(x,sales,'r')
# plt.plot(x,jan_sales,'g',lw=5)

#柱状图
plt.bar(range(len(sales)),sales,0.4,color='b',alpha=0.8)
plt.ylabel('销量')
plt.title('水果11月销量')
plt.xticks(range(len(sales)),x)
plt.ylim([100,1500])
for x,y in enumerate(sales):
    plt.text(x,y+50,'%s'%y,ha='center')

plt.show()
