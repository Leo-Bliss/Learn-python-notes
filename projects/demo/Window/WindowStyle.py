#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    9:34  2019/12/4
#@Author  :    tb_youth
#@FileName:    WindowStyle.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
窗口，绘图特效：设置窗口风格
只改变控件的风格
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore


class WindowStyleDemo(QWidget):
    def __init__(self):
        super().__init__()
        # self.resize(800,800)
        self.setWindowTitle('设置窗口风格')
        hlyaout = QHBoxLayout()
        self.style_label = QLabel('设置窗口风格：')
        self.style_combox = QComboBox()
        self.style_combox.addItems(QStyleFactory.keys())

        #获取当前窗口风格
        print(QApplication.style().objectName())
        index = self.style_combox.findText(QApplication.style().objectName(),QtCore.Qt.MatchFixedString)
        self.style_combox.setCurrentIndex(index)


        self.style_combox.activated[str].connect(self.handleStyleChanged)

        #布局
        hlyaout.addWidget(self.style_label)
        hlyaout.addWidget(self.style_combox)
        self.setLayout(hlyaout)


    def handleStyleChanged(self,style):
        QApplication.setStyle(style)



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = WindowStyleDemo()
    window.show()
    sys.exit(app.exec_())