#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/6 0006 19:39
#@Author  :    tb_youth
#@FileName:    DrawApp.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
项目实战：实现绘图应用
1.如何绘图
2.在哪里绘图
3.如何通过鼠标移动绘图

鼠标有3个事件：
鼠标按下
鼠标移动
鼠标抬起
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import QPainter,QPixmap

class DrawApp(QWidget):
    def __init__(self,parent=None):
        super(QWidget,self).__init__(parent)
        self.pix = QPixmap()
        self.last_point = QPoint()
        self.end_point = QPoint()
        self.initUI()

    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('画板1.0')
        #设置画布,大小，背景色
        self.pix = QPixmap(self.size())
        self.pix.fill(Qt.white)


    def paintEvent(self,event):
        painter = QPainter(self.pix)
        #根据鼠标指针前后位置绘制一条直线
        painter.drawLine(self.last_point,self.end_point)
       #画完一条直线，开始点为之前结束点
        self.last_point = self.end_point
        painter2 = QPainter(self)
        painter2.drawPixmap(0,0,self.pix)

    #按下时，设置开始点为动态点
    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()

    # 按着移动时要一直画，同时要让目标点为动态点
    def mouseMoveEvent(self,event):
        if event.buttons() and Qt.LeftButton:
            self.end_point = event.pos()
            self.update()

    # # 鼠标左键释放，结束点设设置
    # #这里也可以不写，原因是结束点在移动的时候动态更新
    # def mouseReleaseEvent(self,event):
    #     if event.button() == Qt.LeftButton:
    #         self.end_point = event.pos()
    #         self.update()



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = DrawApp()
    window.show()
    sys.exit(app.exec_())
