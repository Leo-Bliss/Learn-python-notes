#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/26 0026 18:57
#@Author  :    tb_youth
#@FileName:    LineEditdemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class LineEditDemo(QWidget):
    def __init__(self):
        super(LineEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('LineEditDemo')

        #第一个输入框int校验，输入数字不超过9999
        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setFont(QFont('Arial',20))

        #第二个浮点校验
        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))

        #第三个设置输入掩码
        edit3 = QLineEdit()
        edit3.setInputMask('9999-99-99;#')


        #第四个绑定信号
        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChange)

        # 第五个密码输入
        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)

        #第六个只读模式
        edit6 = QLineEdit('read only~')
        edit6.setReadOnly(True)

        #布局
        form_layout = QFormLayout()
        form_layout.addRow('整数校验：',edit1)
        form_layout.addRow('浮点型校验：',edit2)
        form_layout.addRow('输入掩码：',edit3)
        form_layout.addRow('文本变化：',edit4)
        form_layout.addRow('密码输入：',edit5)
        form_layout.addRow('只读：',edit6)
        self.setLayout(form_layout)

    def textChange(self,text):
        print('输入的内容是:',text)

    def enterPress(self):
        print('输入完成')



if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = LineEditDemo()
    window.show()
    sys.exit(app.exec_())

