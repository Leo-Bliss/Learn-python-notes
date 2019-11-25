#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    15:54  2019/11/25
#@Author  :    tb_youth
#@FileName:    DockWidget1.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class DockWidgetDemo(QMainWindow):
    def __init__(self):
        super(DockWidgetDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('窗口停靠')

        layout= QHBoxLayout()
        self.items = QDockWidget('DockWidget',self)
        self.listWidget = QListWidget()
        for i in range(5):
            self.listWidget.addItem('item%s'%i)
        self.items.setWidget(self.listWidget)
        self.setCentralWidget(QLineEdit())
        #设置默认悬浮
        # self.items.setFloating((True))

        self.addDockWidget(Qt.RightDockWidgetArea,self.items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DockWidgetDemo()
    window.show()
    sys.exit(app.exec_())