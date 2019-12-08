#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/8 0008 13:52
#@Author  :    tb_youth
#@FileName:    LoadQSS.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
动态装置QSS文件
'''

import sys
from PyQt5.QtWidgets import *
from projects.demo.BasicQSS.CommonHelper import CommonHelper

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle('装载QSS')
        self.resize(800, 500)
        self.button = QPushButton('btn')
        self.button.setToolTip('Hint 2333~')
        vbox = QVBoxLayout()
        vbox.addWidget(self.button)
        self.button.clicked.connect(self.onClicked)

        widget  = QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(vbox)



    def onClicked(self):
        style_file = './style.qss'
        qssStyle = CommonHelper.readQSS(style_file)
        # print(qssStyle)
        self.setStyleSheet(qssStyle)




if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())