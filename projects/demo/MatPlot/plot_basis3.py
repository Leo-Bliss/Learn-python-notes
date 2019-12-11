#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/11 0011 20:19
#@Author  :    tb_youth
#@FileName:    plot_basis3.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
绘制饼图
'''

import matplotlib.pyplot as plt

#防止中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#将坐标标准化，保证饼图为正圆
plt.axes(aspect='equal')

#坐标轴范围
plt.xlim(0,5)
plt.ylim(0,5)

#绘制饼图

#设置绘制风格
plt.style.use('ggplot')
labels = ['高数','线代','C++','英语']
data = [90,88,99,85]
explode = [0,0,0.1,0,] # 用于突出显示
colors=['#FEB748','#EDD25D','#FE4F54','#51B4FF','#dd5555'] # 自定义颜色
plt.pie(x=data,#数据
        explode=explode,
        labels = labels,#标签
        autopct='%.1f%%',#百分比格式
        pctdistance=0.6,#百分比标签离圆心距离
        startangle=180,#设置饼图初始角度
        labeldistance=5,#设置水平标签与圆心的距离
        radius=1.5,#设置饼图的半径
        counterclock=False,#是否逆时针
        wedgeprops={'linewidth':1.5,'edgecolor':'yellow'},#饼图外边界
        textprops={'fontsize':12,'color':'k'},#设置文本标签属性
        center = (2.5,2.5),#设置饼图原点
        frame = True,#是否显示饼图圆框

        )

#删除坐标轴刻度
plt.xticks(())
plt.yticks(())

#把边框颜色去掉，直接去掉frame，title容易异位
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['left'].set_color('none')
plt.gca().spines['bottom'].set_color('none')

#添加图标题
plt.title('某某2020年第一学期成绩占比情况',ha='center')

plt.show()
