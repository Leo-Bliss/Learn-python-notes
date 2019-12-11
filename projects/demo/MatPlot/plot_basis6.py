#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/11 0011 21:30
#@Author  :    tb_youth
#@FileName:    plot_basis6.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
绘制雷达图
'''

import matplotlib.pyplot as plt
import numpy as np

labels = np.array(['C/C++','Java','Python','Go','PHP','HTML','CSS'])
n = labels.size
data = np.array([8,5,6,2,3,5,3])
angles = np.linspace(0,2*np.pi,n,endpoint=False)
data = np.concatenate((data,[data[0]]))
angles = np.concatenate((angles,[angles[0]]))

fig = plt.figure()
ax = fig.add_subplot(111,polar=True)
ax.plot(angles,data,'bo-',linewidth=2)
ax.fill(angles,data,facecolor='r',alpha=0.25)
ax.set_thetagrids(angles*180/np.pi,labels,fontproperties='SimHei')
ax.set_title('编程语言熟悉度',va = 'bottom',fontproperties='SimHei')
ax.set_rlim(0,10)
ax.grid(True)
plt.show()
