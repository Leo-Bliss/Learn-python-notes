#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/3/1 0001 23:49
#@Author  :    tb_youth
#@FileName:    Splitter.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
控件大小可动态调整，splitter(分离器)
QSplitter(分离器):拖动控件之间的边界
'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QSplitter,QFrame
from PyQt5.QtWidgets import QHBoxLayout,QTextEdit
from PyQt5.QtCore import Qt
class Splitter(QWidget):
    def __init__(self):
        super(Splitter, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        topLeft = QFrame()
        topLeft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        text = QTextEdit()
        splitter1.addWidget(topLeft)
        splitter1.addWidget(text)
        splitter1.setSizes([200,200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Splitter()
    window.show()
    sys.exit(app.exec_())
