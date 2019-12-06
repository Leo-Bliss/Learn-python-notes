#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/6 0006 21:33
#@Author  :    tb_youth
#@FileName:    QSS1.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
QSS基础
QSS (Qt Style Sheets)
Qt样式
用于设置控件样式
CSS类似
'''

import sys
from PyQt5.QtWidgets import *

class QCSSDemo1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300,300)
        self.setWindowTitle('QSS1')

        button1 = QPushButton('按钮1')
        button2 = QPushButton('按钮2')

        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(button1)
        vboxlayout.addWidget(button2)
        self.setLayout(vboxlayout)

if __name__ =='__main__':
    app = QApplication(sys.argv)
    qssStyle = '''
    QPushButton{
    background-color:blue;
    font-size:25px;
    }
    '''
    window = QCSSDemo1()
    window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())