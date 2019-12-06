#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/6 0006 18:53
#@Author  :    tb_youth
#@FileName:    WindowMaxMin.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
代码控制窗口最大化与最小化

'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class WindowMaxMinDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('Control Window Max and Min')
        # #默认最大最小关闭都显示，这里设置一个则只会显示一个
        # self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint|Qt.WindowMaximizeButtonHint|Qt.WindowCloseButtonHint)
        #自己编写信号代码
        button_min = QPushButton()
        button_min.setText('窗口最小化')
        button_max = QPushButton()
        button_max.setText('窗口最大化')
        button_close = QPushButton()
        button_close.setText('窗口关闭')
        hlayout = QHBoxLayout()
        hlayout.addWidget(button_min)
        hlayout.addWidget(button_max)
        hlayout.addWidget(button_close)
        self.setLayout(hlayout)

        #关联信号
        button_min.clicked.connect(self.setMinWindow)
        button_max.clicked.connect(self.setMaxWindow)
        button_close.clicked.connect(self.setWindowClose)

    def setMinWindow(self):
        self.showMinimized()

    def setMaxWindow(self):
        # self.showMaximized()
        desktop = QApplication.desktop()
        #获取桌面可用尺寸
        rect = desktop.availableGeometry()
        self.setGeometry(rect)

    def setWindowClose(self):
        self.close()



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = WindowMaxMinDemo()
    window.show()
    sys.exit(app.exec_())
