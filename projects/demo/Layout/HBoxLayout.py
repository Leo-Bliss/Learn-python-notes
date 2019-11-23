#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/16 0016 21:54
#@Author  :    tb_youth
#@FileName:    HBoxLayout.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth
'''
水平布局：
设置控件间隔
控制控件对齐方式

'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QPushButton
from PyQt5.QtCore import Qt

class HBoxLayoutDemo(QWidget):
    def __init__(self):
        super(HBoxLayoutDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('HBoxLayoutDemo')

        hlayout = QHBoxLayout()
        # for i in range(1,5):
        #     hlayout.addWidget(QPushButton(str(i)))
        #(self, QWidget, stretch=0, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None, *args, **kwargs)
        hlayout.addWidget(QPushButton('1'),1,Qt.AlignLeft | Qt.AlignTop)
        hlayout.addWidget(QPushButton('2'),1,Qt.AlignLeft | Qt.AlignTop)
        hlayout.addWidget(QPushButton('3'),1,Qt.AlignLeft | Qt.AlignCenter)
        hlayout.addWidget(QPushButton('4'),1,Qt.AlignRight | Qt.AlignBottom)
        hlayout.addWidget(QPushButton('5'),0,Qt.AlignRight | Qt.AlignBottom)
        #控件间隔
        hlayout.setSpacing(20)
        self.setLayout(hlayout)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = HBoxLayoutDemo()
    window.show()
    sys.exit(app.exec_())





