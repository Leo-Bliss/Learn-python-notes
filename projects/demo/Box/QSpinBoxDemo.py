#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/7 0007 22:43
#@Author  :    tb_youth
#@FileName:    QSpinBoxDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
计数器控件
'''

import sys
from PyQt5.QtWidgets import QApplication,QSpinBox,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt
class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(500,200)
        self.setWindowTitle('QSpinBoxDemo')

        self.label = QLabel('current value:')
        self.label.setAlignment(Qt.AlignCenter)

        self.spinbox = QSpinBox()
        #设置值
        self.spinbox.setValue(6)
        self.spinbox.setRange(5,100)
        #设置步长
        self.spinbox.setSingleStep(2)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        self.spinbox.valueChanged.connect(self.valueChange)

    def valueChange(self):
        self.label.setText('current value:'+str(self.spinbox.value()))


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = QSpinBoxDemo()
    window.show()
    sys.exit(app.exec_())