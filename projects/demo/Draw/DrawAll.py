#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    11:18  2019/11/22
#@Author  :    tb_youth
#@FileName:    DrawAll.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
绘制各种图形：
弧，圆形，椭圆，矩形，多边形，绘制图像
'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont,QPen,QPolygon,QImage
from PyQt5.QtCore import Qt,QRect,QPoint

class DrawAllDemo(QWidget):
    def __init__(self):
        super(DrawAllDemo,self).__init__()
        self.resize(600,600)
        self.setWindowTitle('绘制各种图形')

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        #绘制弧
        #左上角位置，宽度，高度
        rect = QRect(0,10,100,100)
        #alen:1 alen=1/16度 45*16=720
        painter.drawArc(rect,0,50*16)

        #绘制圆
        painter.setPen(Qt.red)
        painter.drawArc(120,10,100,100,0,360*16)
        #绘制带弦的弧
        painter.drawChord(10,120,100,100,12,130*16)
        #绘制扇形
        painter.drawPie(10,240,100,100,12,130*16)
        #绘制椭圆
        painter.drawEllipse(120,120,150,100)
        #5边形
        point1 = QPoint(140,380)
        point2 = QPoint(270,420)
        point3 = QPoint(219, 512)
        point4 = QPoint(290, 588)
        point5 = QPoint(120, 533)
        polygon = QPolygon([point1,point2,point3,point4,point5])
        painter.drawPolygon(polygon)

        #绘制图像
        image = QImage('./school.jpg')
        rect = QRect(300,200,image.width()/2,image.height()/2)
        painter.drawImage(rect,image)
        # image.save('./school1.png')
        painter.end()


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = DrawAllDemo()
    window.show()
    sys.exit(app.exec_())