#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/30 0030 14:28
#@Author  :    tb_youth
#@FileName:    OverrideSlot.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
Qoverride (覆盖)槽函数
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class OverrideSlotDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Override覆盖槽函数')

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Alt:
            self.setWindowTitle('Alt被按下')



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = OverrideSlotDemo()
    window.show()
    sys.exit(app.exec_())