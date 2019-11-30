#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/30 0030 14:34
#@Author  :    tb_youth
#@FileName:    MulitWindow1.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
多窗口交互（1）：不使用信号与槽
win1

win2

'''

import sys
from PyQt5.QtWidgets import *
from DateDialog import DateDialogDemo


class MulitWindowDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('多窗口交互（1）：不使用信号与槽')

        self.line_edit = QLineEdit(self)
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.onButton1Clicked)

        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.onButton2Clicked)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.line_edit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)
        self.setLayout(gridLayout)
    def onButton1Clicked(self):
        dialog = DateDialogDemo(self)
        result = dialog.exec_()
        date = dialog.dateTime()
        self.line_edit.setText(date.date().toString())
        dialog.destroy()

    def onButton2Clicked(self):
        date,time,result = DateDialogDemo.getDateTime()
        self.line_edit.setText(date.toString())

        if result == QDialog.Accepted:
            print('点击确定按钮')
        else:
            print('点击取消按钮')


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MulitWindowDemo()
    window.show()
    sys.exit(app.exec_())




