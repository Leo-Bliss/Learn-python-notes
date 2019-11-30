
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/30 0030 13:08
#@Author  :    tb_youth
#@FileName:    ThreadUpdateUI.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth


'''
多线程更新UI数据
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
import sys

class BackendThread(QThread):
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            current_time = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(current_time))
            time.sleep(1)


class TreadUpdateUIDemo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(500,500)
        self.setWindowTitle('多线程更新UI数据')
        self.input = QLineEdit(self)
        self.input.resize(400,100)

        self.initUI()

    def initUI(self):
        self.backed = BackendThread()
        self.backed.update_date.connect(self.handleDisplay)
        self.backed.start()

    def handleDisplay(self,data):
        self.input.setText(data)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = TreadUpdateUIDemo()
    window.show()
    sys.exit(app.exec_())
