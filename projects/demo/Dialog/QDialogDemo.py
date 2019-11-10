#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/10 0010 22:13
#@Author  :    tb_youth
#@FileName:    QDialogDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QDialog
from PyQt5.QtCore import Qt
import sys
class QDialogDemo(QWidget):
    def __init__(self):
        super(QDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('QDialogDemo')

        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(50,50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton('确定',dialog)
        button.clicked.connect(dialog.close)
        button.move(50,50)
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = QDialogDemo()
    window.show()
    sys.exit(app.exec_())
