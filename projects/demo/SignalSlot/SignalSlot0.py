#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/29 0029 22:05
#@Author  :    tb_youth
#@FileName:    SignalSlot0.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

class SignalSlotDemo(QWidget):
    def __init__(self):
        super(SignalSlotDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,400)
        self.setWindowTitle('信号与槽')
        self.btn = QPushButton('我的按钮',self)
        self.btn.clicked.connect(self.onClicked)

    def onClicked(self):
        self.btn.setText('信号已发出')
        self.btn.setStyleSheet("QPushButton(max-width:200px;min-width:200px)")


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = SignalSlotDemo()
    window.show()
    sys.exit(app.exec_())
