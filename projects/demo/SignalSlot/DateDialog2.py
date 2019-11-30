#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/30 0030 15:18
#@Author  :    tb_youth
#@FileName:    DateDialog2.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class DateDialogDemo2(QDialog):
    Signal_OneParameter = pyqtSignal(str)
    def __init__(self,parent=None):
        super(DateDialogDemo2,self).__init__(parent)
        self.setWindowTitle('DateDialog')

        layout = QVBoxLayout()

        lable = QLabel('前者发送内置信号\n后者发送自定义信号')
        self.datetime_inner = QDateTimeEdit(self)
        self.datetime_inner.setCalendarPopup(True)
        self.datetime_inner.setDateTime(QDateTime.currentDateTime())

        self.datetime_emit = QDateTimeEdit(self)
        self.datetime_emit.setCalendarPopup(True)
        self.datetime_emit.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(lable)
        layout.addWidget(self.datetime_inner)
        layout.addWidget(self.datetime_emit)


        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal,self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.datetime_emit.dateChanged.connect(self.emit_signal)

        layout.addWidget(buttons)
        self.setLayout(layout)

    def dateTime(self):
        return self.datetime_emit.dateTime()

    def emit_signal(self):
        date_str = self.dateTime().toString()
        self.Signal_OneParameter.emit(date_str)







if __name__=='__main__':
    app = QApplication(sys.argv)
    window = DateDialogDemo2()
    window.show()
    sys.exit(app.exec_())
