#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    11:04  2019/11/22
#@Author  :    tb_youth
#@FileName:    DrawLines.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QPen
from PyQt5.QtCore import Qt


class DrawLinesDemo(QWidget):
    def __init__(self):
        super(DrawLinesDemo,self).__init__()
        self.resize(300,300)
        self.setWindowTitle('设置Pen的样式')

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.red,3,Qt.SolidLine)
        painter.setPen(pen)
        # 两端点的坐标(x1,y1) (x2,y2)
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        #自定义
        pen.setStyle(Qt.CustomDashLine)
        #相对宽度
        pen.setDashPattern([1,10,5,8])
        painter.setPen(pen)
        painter.drawLine(20,200,250,200)
        painter.end()



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = DrawLinesDemo()
    window.show()
    sys.exit(app.exec_())