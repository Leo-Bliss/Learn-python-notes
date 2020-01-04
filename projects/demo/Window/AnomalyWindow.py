#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/1/4 0004 23:10
#@Author  :    tb_youth
#@FileName:    AnomalyWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
异形窗口：
通过mask 实现异形窗口
原理：图片透明部分被抠出，形成一个不规则区域
并且实现窗口的移动,关闭
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QAction,QToolBar
from PyQt5.QtGui import QBitmap,QPainter,QPixmap,QCursor
from PyQt5.QtCore import Qt


class AnomalyWindow(QWidget):
    def __init__(self):
        super(AnomalyWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("异形窗口")
        self.pix = QBitmap('./image/mask.png')
        self.resize(self.pix.size())
        #设置mask
        self.setMask(self.pix)


    #设置异形窗口背景
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap('./image/screen1.jpg'))

    #鼠标按下事件
    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            #鼠标左键按下，开始拖动
            self.m_drag = True

            #按下点相对屏幕的坐标
            print(event.globalPos())
            #按下点相对窗口坐标，不包含标题栏
            print(event.pos())
            #窗口左上角坐标
            print(self.pos())

            #按下点相对窗口坐标，包含标题栏
            self.m_drapPosition = event.globalPos() - self.pos()
            #光标样式
            self.setCursor(QCursor(Qt.OpenHandCursor))

        if event.button() == Qt.RightButton:
                self.close()

    def mouseMoveEvent(self,event):
        #实时计算窗口左上角坐标(要减去包含标题栏的坐标)
        self.move(event.globalPos()-self.m_drapPosition)

    def mouseReleaseEvent(self,event):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))




if __name__=='__main__':
    app = QApplication(sys.argv)
    window = AnomalyWindow()
    window.show()
    sys.exit(app.exec_())
