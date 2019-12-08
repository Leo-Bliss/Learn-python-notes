#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/8 0008 13:48
#@Author  :    tb_youth
#@FileName:    OpacityWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
设置透明窗口
Opacity:不透明度（0-1）
'''

import sys
from PyQt5.QtWidgets import *

class OpacityWindowDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('设置窗口透明度')
        self.setWindowOpacity(0.6)
        self.button = QPushButton('btn',self)
        self.resize(500,500)



if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = OpacityWindowDemo()
    window.show()
    sys.exit(app.exec_())