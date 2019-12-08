#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/8 0008 12:55
#@Author  :    tb_youth
#@FileName:    LabelButtonBackground.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
使用QSS为标签和按钮添加背景图
'''
import sys
from PyQt5.QtWidgets import *

class LabelButtonBackground(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('为标签与按钮添加背景')
        self.resize(500,500)
        label = QLabel(self)
        label.setToolTip('this is a  label')
        label.setStyleSheet('QLabel{border-image:url(./images/bkg0.jpg);}')

        label.setFixedSize(476,259)

        btn1 = QPushButton(self)
        btn1.setObjectName('btn1')
        btn1.setMaximumSize(200,200)
        btn1.setMinimumSize(200,200)

        style = '''
        #btn1{
        border-radius:4px;
        background-image:url('./images/0.png');
        }
        #btn1:Pressed{
        background-image:url('./images/1.png');
        }
        '''
        btn1.setStyleSheet(style)
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addStretch()
        vbox.addWidget(btn1)
        self.setLayout(vbox)


if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = LabelButtonBackground()
    window.show()
    sys.exit(app.exec_())





