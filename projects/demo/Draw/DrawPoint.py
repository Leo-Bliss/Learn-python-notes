#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    10:49  2019/11/22
#@Author  :    tb_youth
#@FileName:    DrawPoint.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''

drawPoint(x,y)
'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt
import math

class DrawPointDemo(QWidget):
    def __init__(self):
        super(DrawPointDemo,self).__init__()
        self.resize(300,300)
        self.setWindowTitle('绘制两个周期的正弦曲线')

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        size = self.size()
        for i in range(1000):
            #size.width()/2.0,size.height()/2.0目的是使0点在窗口中心
            x = 100 * (-1 + 2.0 * i / 1000) + size.width()/2.0
            y = -50 * math.sin((x - size.width()/2.0) * math.pi/50) + size.height()/2.0
            painter.drawPoint(x,y)
        painter.end()



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = DrawPointDemo()
    window.show()
    sys.exit(app.exec_())