#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    21:18  2019/12/12
#@Author  :    tb_youth
#@FileName:    PlotOnWindow.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
在窗口中使用matlibplot绘制图形
'''
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QPushButton, QVBoxLayout,QWidget,QTextEdit
import matplotlib.pyplot as plt
import sys


class PlotWindowDemo(QWidget):
    def __init__(self):
        super(PlotWindowDemo,self).__init__()
        #创建一个展示板
        self.figure = plt.figure(facecolor='#66CCFF')
        self.canvas = FigureCanvas(self.figure)
        self.draw_button = QPushButton("绘图")
        #显示用于分析的数据
        self.text_edit = QTextEdit()

        #绑定信号
        self.draw_button.clicked.connect(self.onClickDraw)

        #设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.draw_button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        layout.addWidget(self.text_edit)

    def onClickDraw(self):
        #这里开始就按照matlibplot的方式绘图
        data1 = [2211, 2323, 1560, 7788, 3322, 1000, 7089]
        data2 = [1235, 3456, 666, 8886, 2323, 3000, 223]
        # 中文乱码处理
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        x = [str(i) + 'h' for i in range(1, len(data1) + 1)]

        plt.plot(x, data1, marker='*', mec='r', label='股票1')
        plt.plot(x, data2, marker='o', mec='b', lw=2, label='股票2')

        # label显示
        plt.legend()

        # x轴标签
        plt.xticks(x)

        plt.ylim(100, 10000)

        # 标上数值
        for x, y in enumerate(data1):
            plt.text(x, y + 100, '%s' % y, ha='center')

        for x, y in enumerate(data2):
            plt.text(x, y + 500, '%s' % y, ha='center')

        #设置标题
        plt.title("股票价格波动")

        #按照matlibplot的方式绘制之后，在窗口上绘制
        self.canvas.draw()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = PlotWindowDemo()
    main_window.show()
    app.exec()


