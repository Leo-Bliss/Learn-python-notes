#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/3/2 0002 21:50
#@Author  :    tb_youth
#@FileName:    Counter.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth
'''
使用QThread编写计数器
'''

from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from PyQt5.QtWidgets import QLCDNumber,QVBoxLayout,QPushButton
from PyQt5.QtCore import QThread,pyqtSignal
import  sys

class WorkThread(QThread):
    send = pyqtSignal(int)
    finished = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.sec = 0

    def run(self):
        while True:
            self.sleep(1)
            self.sec += 1
            self.send.emit(self.sec)
            if self.sec == 5:
                break
        self.finished.emit()


class Counter(QWidget):
    def __init__(self):
        super(Counter, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("使用QThread编写计数器")
        self.resize(300,300)
        layout = QVBoxLayout()
        self.lcdNumer = QLCDNumber()
        self.button = QPushButton("开始计数")
        layout.addWidget(self.lcdNumer)
        layout.addWidget(self.button)

        self.workThread = WorkThread()
        self.workThread.send.connect(self.countTime)
        self.workThread.finished.connect(self.endCount)
        self.button.clicked.connect(self.work)
        self.setLayout(layout)

    def countTime(self,sec):
        self.lcdNumer.display(str(sec))

    def endCount(self):
        QMessageBox.information(self,'消息','计数结束',QMessageBox.Ok)
        self.workThread.quit()

    def work(self):
        self.workThread.start()






if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Counter()
    window.show()
    sys.exit(app.exec_())



