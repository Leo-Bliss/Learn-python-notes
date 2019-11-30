#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/30 0030 14:38
#@Author  :    tb_youth
#@FileName:    DateDialog.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class DateDialogDemo(QDialog):
    def __init__(self,parent=None):
        super(DateDialogDemo,self).__init__(parent)
        self.setWindowTitle('DateDialog')

        layout = QVBoxLayout()
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal,self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)
        self.setLayout(layout)

    def dateTime(self):
        return self.datetime.dateTime()

    @staticmethod
    def getDateTime(parent=None):
        dialog = DateDialogDemo(parent)
        result = dialog.exec_()
        date = dialog.dateTime()
        return (date.date(),date.time(),result==QDialog.Accepted)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = DateDialogDemo()
    window.show()
    sys.exit(app.exec_())