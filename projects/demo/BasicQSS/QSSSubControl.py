#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/7 0007 18:36
#@Author  :    tb_youth
#@FileName:    QSSSubControl.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
QSS子控件选择器

QComboBox
'''

import sys
from PyQt5.QtWidgets import *

class QSSSubControlDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(600,600)
        self.setWindowTitle('子控件选择器')

        comboBox = QComboBox(self)
        comboBox.setObjectName("myComboBox")
        comboBox.addItems(['Linux','Windows','Mac OS X'])

        comboBox.move(200,300)



if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = QSSSubControlDemo()
    qssStyle = '''
    QComboBox#myComboBox::drop-down{
    image:url(./images/drop_down.png)
    }
    '''
    window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())