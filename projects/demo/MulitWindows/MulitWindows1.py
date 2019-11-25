#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    16:14  2019/11/25
#@Author  :    tb_youth
#@FileName:    MulitWindows1.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth
'''
QMdiArea
QMdiSubWindow
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MulitWindowsDemo(QMainWindow):
    count = 0
    def __init__(self):
        super(MulitWindowsDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('多窗口')

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('New')
        file.addAction('Cascade')
        file.addAction('Tiled')

        file.triggered.connect(self.windowAction)

    def windowAction(self,q):
        if q.text() == 'New':
            MulitWindowsDemo.count = MulitWindowsDemo.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle('子窗口'+str(MulitWindowsDemo.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == 'Cascade':
            self.mdi.cascadeSubWindows()
        else:
            self.mdi.tileSubWindows()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MulitWindowsDemo()
    window.show()
    sys.exit(app.exec_())