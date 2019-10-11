#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QWidget,QPushButton

def onClick_Button():
    print('onclick')
    #不带窗口边框
    print('(widget.x,widget.y) = ',(widget.x(),widget.y()))#（250,200）
    print('(widget.w,widget.h) = ',(widget.width(),widget.height()))#（300,400）

    #带窗口边框（边框宽：1px，高：38px）工作区
    print('(widget.geometry.x,widget.geometry.y) = ',\
              (widget.geometry().x(), widget.geometry().y()))#（251,238）
    print('(widget.geometry.w,widget.geometry.h) = ',\
          (widget.geometry().width(), widget.geometry().height()))#（300,240）
    #窗口
    print('(widget.frameGeometry.x,widget.frameGeometry.y) = ', \
          (widget.frameGeometry().x(), widget.frameGeometry().y()))  # （250,200）窗口坐标
    print('(widget.frameGeometry.w,widget.frameGeometry.h) = ',\
          (widget.frameGeometry().width(), widget.frameGeometry().height()))  # （302,279）窗口size

app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClick_Button)

btn.move(24,52)

widget.resize(300,240) #设置工作区的size
widget.move(250,200)
widget.setWindowTitle('Geometry')
widget.show()
sys.exit(app.exec_())

