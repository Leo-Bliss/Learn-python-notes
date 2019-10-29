#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/26 0026 21:32
#@Author  :    tb_youth
#@FileName:    QRadioButtonDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import QRadioButton,QApplication,QWidget,QHBoxLayout


class RadioButtonDemo(QWidget):
    def __init__(self):
        super(RadioButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(400,200)
        self.setWindowTitle('RadioButton')

        self.radio_button1 = QRadioButton('单选按钮1')
        self.radio_button1.setChecked(True)
        self.radio_button1.toggled.connect(self.buttonStatus)

        self.radio_button2 = QRadioButton('单选按钮2')
        self.radio_button2.toggled.connect(self.buttonStatus)

        layout = QHBoxLayout()
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)
        self.setLayout(layout)

    def buttonStatus(self):
        # if self.radio_button1.isChecked():
        #     print('1111111111')
        # else:
        #     pass
        radio_button = self.sender()
        if radio_button.text() == '单选按钮1':
            if radio_button.isChecked() == True:
                print(radio_button.text() + '被选中')
            else:
                print(radio_button.text() + '选中取消')
        if radio_button.text() == '单选按钮2':
            if radio_button.isChecked() == True:
                print(radio_button.text() + '被选中')
            else:
                print(radio_button.text() + '选中取消')



if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = RadioButtonDemo()
    window.show()
    sys.exit(app.exec_())