#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/30 0030 12:59
#@Author  :    tb_youth
#@FileName:    WinSignal.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
import sys

class WinSignal(QWidget):
    button_clicked_signal = pyqtSignal()

    def __init__(self):
        super(WinSignal,self).__init__()
        self.resize(500,500)
        self.setWindowTitle('为窗口添加信号')
        btn = QPushButton('关闭窗口',self)
        btn.clicked.connect(self.btnClicked)
        self.button_clicked_signal.connect(self.btnClose)

    def btnClicked(self):
        self.button_clicked_signal.emit()

    def btnClose(self):
        print('close')
        self.close()



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = WinSignal()
    window.show()
    sys.exit(app.exec_())