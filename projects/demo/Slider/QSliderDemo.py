#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/5 0005 23:13
#@Author  :    tb_youth
#@FileName:    QSliderDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QSlider,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('QSliderDemo')

        self.label = QLabel('Hello,PYQT5')
        self.label.setAlignment(Qt.AlignCenter)

        #水平滑块
        self.hslider = QSlider(Qt.Horizontal)
        #设置最小值
        self.hslider.setMinimum(30)
        #设置最大值
        self.hslider.setMaximum(50)
        #步长
        self.hslider.setSingleStep(3)
        #当前值
        self.hslider.setValue(18)
        #设置刻度的位置，刻度在下方
        self.hslider.setTickPosition(QSlider.TicksBelow)
        #设置刻度间隔
        self.hslider.setTickInterval(6)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.hslider)
        self.setLayout(layout)

        self.hslider.valueChanged.connect(self.valueChange)

    def valueChange(self):
        print('current value',self.hslider.value())
        size = self.hslider.value()
        self.label.setFont(QFont('Arial',size))




if __name__=='__main__':
    app = QApplication(sys.argv)
    window = QSliderDemo()
    window.show()
    sys.exit(app.exec_())