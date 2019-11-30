#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/30 0030 15:16
#@Author  :    tb_youth
#@FileName:    MulitWindow2.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth


'''
多窗口交互（1）：使用信号与槽
win1

win2

'''

import sys
from PyQt5.QtWidgets import *
from DateDialog2 import DateDialogDemo2


class MulitWindowDemo2(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,200)
        self.setWindowTitle('多窗口交互（1）：使用信号与槽')

        self.line_edit = QLineEdit(self)
        self.line_edit2 = QLineEdit(self)
        self.line_edit.setText('接收子窗口内置信号的时间')
        self.line_edit2.setText('接收子窗口自定义信号的时间')
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.openDialog)


        gridLayout = QGridLayout()
        gridLayout.addWidget(self.line_edit)
        gridLayout.addWidget(self.line_edit2)
        gridLayout.addWidget(self.button1)
        self.setLayout(gridLayout)

    def openDialog(self):
        dialog = DateDialogDemo2(self)
        dialog.datetime_inner.dateTimeChanged.connect(self.deal_inner_slot)
        dialog.Signal_OneParameter.connect(self.deal_emit_slot)
        dialog.show()

    def deal_inner_slot(self,date):
        self.line_edit.setText(date.toString())

    def deal_emit_slot(self,date_str):
        self.line_edit2.setText(date_str)



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MulitWindowDemo2()
    window.show()
    sys.exit(app.exec_())




