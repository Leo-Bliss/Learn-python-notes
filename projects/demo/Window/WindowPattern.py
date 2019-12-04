#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    10:00  2019/12/4
#@Author  :    tb_youth
#@FileName:    WindowPattern.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
设置窗口样式：
主要是窗口边框，标题了以及窗口本身样式
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

class WindowPatternDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('设置窗口样式')
        #无边框： | Qt.FramelessWindowHint
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
        self.setObjectName('MainWindow')
        self.setStyleSheet('#MainWindow{border-image:url(images/bkg1.jpg);}')



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = WindowPatternDemo()
    window.show()
    sys.exit(app.exec_())