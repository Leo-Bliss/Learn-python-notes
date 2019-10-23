#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/22 0022 10:51
#@Author  :    tb_youth
#@FileName:    StatusBar.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

from PyQt5.QtWidgets import QApplication,QMainWindow,QStatusBar,QMenuBar,QTextEdit,QMessageBox
from PyQt5.QtGui import QIcon
import sys
class StatusBarDemo(QMainWindow):
    def __init__(self):
        super(StatusBarDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('StatusBarDemo')
        self.setWindowIcon(QIcon('./photos/分析 (1).png'))

        self.status = QStatusBar()
        # self.status.showMessage('122222',5000)
        self.setStatusBar(self.status)

        #菜单栏
        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('show')
        file.addAction('new')
        file.triggered.connect(self.pressTrigger)
        self.setCentralWidget(QTextEdit())

    def pressTrigger(self,q):
        if(q.text()=='show'):
            self.status.showMessage(q.text()+'菜单被点击',5000)
        else:
            QMessageBox.information(self,'new','this is new')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StatusBarDemo()
    window.show()
    sys.exit(app.exec_())


