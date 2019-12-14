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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.items.setSizePolicy(sizePolicy)
        self.items.setFixedHeight(80)
        self.listWidget = QListWidget()
        for i in range(5):
            self.listWidget.addItem('item%s'%i)
        self.items.setWidget(self.listWidget)
        '''
            在QMainWindow中加入QWidget可以突破QMainWindow中使用其他布局无效的局限,
            同理，在各种窗口中加入其他窗口，可以将窗口展现的更丰富
        '''
        gridLayout = QGridLayout(self)

        widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(QTextEdit())
        gridLayout.addItem(layout)
        widget.setLayout(gridLayout)

        self.setCentralWidget(widget)
        # self.setCentralWidget(QLineEdit())
        #设置默认悬浮
        # self.items.setFloating((True))

        self.addDockWidget(Qt.TopDockWidgetArea,self.items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DockWidgetDemo()
    window.show()
    sys.exit(app.exec_())