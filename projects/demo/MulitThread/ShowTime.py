#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/3/2 0002 21:11
#@Author  :    tb_youth
#@FileName:    ShowTime.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
动态显示时间
QTime，
QThread。
比较耗时的任务，放到另一个线程里面。
多线程，防止阻塞。
多线程：用于同时完成多个任务。
当是单cpu时，是顺序完成任务。
但是系统调度，它会把任务分成好几个片段，
来回切换，从宏观上也是同时完成。
'''

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtCore import QTimer,QDateTime
import sys

class ShowTime(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300,300)
        self.setWindowTitle("动态显示当前时间")
        self.label = QLabel("显示当前时间")
        self.startBtn = QPushButton("开始")
        self.endBtn = QPushButton("结束")
        layout = QGridLayout()

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.setLayout(layout)


    def showTime(self):
        time = QDateTime.currentDateTime()
        time_display = time.toString("yyyy-MM-dd hh:mm:ss:dddd")
        self.label.setText(time_display)

    def startTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = ShowTime()
    window.show()
    sys.exit(app.exec())

