#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/30 0030 14:24
#@Author  :    tb_youth
#@FileName:    PartialSlot.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth


from PyQt5.QtWidgets import *
import sys
from functools import partial


class PartialSlotDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Partial为槽函数传递参数')
        self.resize(500,200)

        button1 = QPushButton('button1')
        button2 = QPushButton('button2')
        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        self.setLayout(layout)

        button1.clicked.connect(partial(self.onButtonClicked,10,20))
        button2.clicked.connect(partial(self.onButtonClicked,10,-20))


    def onButtonClicked(self,m,n):
        print('m + n = ',m+n)
        QMessageBox.information(self,'ans',str(m+n))



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = PartialSlotDemo()
    window.show()
    sys.exit(app.exec_())