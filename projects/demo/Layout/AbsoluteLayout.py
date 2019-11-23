#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/16 0016 21:38
#@Author  :    tb_youth
#@FileName:    AbsoluteLayout.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel

class AbsoluteLayoutDemo(QMainWindow):
    def __init__(self):
        super(AbsoluteLayoutDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('AbsoluteLayout')

        self.label1 = QLabel('深入',self)
        self.label1.move(50,100)

        self.label2 = QLabel('学习',self)
        self.label2.move(100,200)

        self.label3 = QLabel('PyQT5布局',self)
        self.label3.move(150,300)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = AbsoluteLayoutDemo()
    window.show()
    sys.exit(app.exec_())




