#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/30 0030 13:25
#@Author  :    tb_youth
#@FileName:    AutoConnect.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot,self).__init__()
        self.initUI()


    def initUI(self):
        self.okButton = QPushButton('OK',self)
        self.okButton.setObjectName('okButton')
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.okButton)
        self.setLayout(hlayout)

        # self.btn.clicked.connect(self.onClicked)
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    #okButton要和定义的button对象名一致
    #on_objectName_signalName
    def on_okButton_clicked(self):
        print('点击了OK')

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = AutoSignalSlot()
    window.show()
    sys.exit(app.exec_())