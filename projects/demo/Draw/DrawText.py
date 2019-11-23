#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    10:31  2019/11/22
#@Author  :    tb_youth
#@FileName:    DrawText.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
绘图API：绘制文本
1.文本
2.各种图形（直线，点椭圆，弧，扇形，多边形）
3.图像

QPainter

painter = QPainter()
painter.begin()
painter.drawText(...)
painter.end()

必须在paintEven事件方法中绘制各种元素
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt

class DrawTextDemo(QWidget):
    def __init__(self):
        super(DrawTextDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('DrawTextDemo')
        self.text = "python从入门到放弃"

    #它会自动调用
    def paintEvent(self, even):
        painter = QPainter()
        painter.begin(self)
        #设置画笔
        painter.setPen(QColor(255,0,0))
        painter.setFont(QFont('SimSun',25))
        painter.drawText(even.rect(),Qt.AlignCenter,self.text)
        painter.end()



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = DrawTextDemo()
    window.show()
    sys.exit(app.exec_())


