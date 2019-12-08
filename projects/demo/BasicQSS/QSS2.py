#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/7 0007 18:31
#@Author  :    tb_youth
#@FileName:    QSS2.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
只设置某个控件的StyleSheet

'''
import sys
from PyQt5.QtWidgets import *

class QCSSSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300,300)
        self.setWindowTitle('QSS1')

        button1 = QPushButton('按钮1')
        button2 = QPushButton('按钮2')
        button2.setProperty('name','btn2')

        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(button1)
        vboxlayout.addWidget(button2)
        self.setLayout(vboxlayout)

if __name__ =='__main__':
    app = QApplication(sys.argv)
    qssStyle = '''
    QPushButton[name='btn2']{
    background-color:blue;
    font-size:25px;
    color:yellow;
    height:60;
    }
    '''
    window = QCSSSelector()
    window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())