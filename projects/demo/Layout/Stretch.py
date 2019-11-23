#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/16 0016 22:27
#@Author  :    tb_youth
#@FileName:    Stretch.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QHBoxLayout
'''
Stretch:控件间的伸缩量
'''
class StretchDemo(QWidget):
    def __init__(self):
        super(StretchDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(800,100)
        self.setWindowTitle('设置伸缩量')
        bt1 = QPushButton('按钮1',self)
        bt2 = QPushButton('按钮2',self)
        bt3 = QPushButton('按钮3',self)
        bt4 = QPushButton('按钮4',self)
        bt5 = QPushButton('按钮5',self)

        layout = QHBoxLayout()

        layout.addStretch(0)
        layout.addWidget(bt1)
        # layout.addStretch(1)
        layout.addWidget(bt2)
        # layout.addStretch(2)
        layout.addWidget(bt3)
        # layout.addStretch(2)

        layout.addStretch(1)
        layout.addWidget(bt4)
        layout.addWidget(bt5)

        self.setLayout(layout)



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = StretchDemo()
    window.show()
    sys.exit(app.exec_())