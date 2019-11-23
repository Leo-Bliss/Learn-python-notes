#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/16 0016 22:23
#@Author  :    tb_youth
#@FileName:    VBoxLayout.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton


class VBoxLayoutDemo(QWidget):
    def __init__(self):
        super(VBoxLayoutDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('VBoxLayoutDemo')

        vlayout = QVBoxLayout()
        for i in range(1,5):
          vlayout.addWidget(QPushButton(str(i)))
        vlayout.setSpacing(50)
        self.setLayout(vlayout)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = VBoxLayoutDemo()
    window.show()
    sys.exit(app.exec_())
