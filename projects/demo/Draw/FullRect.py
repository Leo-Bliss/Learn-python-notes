#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    14:57  2019/11/22
#@Author  :    tb_youth
#@FileName:    FullRect.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
用画刷填充区域
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont,QPen,QBrush
from PyQt5.QtCore import Qt,QRect,QPoint

class FullRectDemo(QWidget):
    def __init__(self):
        super(FullRectDemo,self).__init__()
        self.resize(600,600)
        self.setWindowTitle('画刷填充区域')

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10,15,90,60)

        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 15, 90, 60)

        brush = QBrush(Qt.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 15, 90, 60)

        brush = QBrush(Qt.HorPattern)
        painter.setBrush(brush)
        painter.drawRect(370, 15, 90, 60)
        painter.end()




if __name__=='__main__':
    app = QApplication(sys.argv)
    window = FullRectDemo()
    window.show()
    sys.exit(app.exec_())