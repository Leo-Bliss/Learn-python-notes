#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/3/2 0002 21:35
#@Author  :    tb_youth
#@FileName:    AutoCloseWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
自动关闭窗口
QTimer.singleShot
'''
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QHBoxLayout
from PyQt5.QtCore import QTimer,Qt

class AutoClose(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("<font color=red size=140><b>窗口将在5秒后自动关闭!</b></font>")
        layout = QHBoxLayout()
        layout.addWidget(label)
        self.timer = QTimer()
        self.timer.singleShot(5000,self.close)
        self.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)
        self.setLayout(layout)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = AutoClose()
    window.show()
    sys.exit(app.exec())


