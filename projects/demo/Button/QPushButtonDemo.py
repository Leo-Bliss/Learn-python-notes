#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/26 0026 20:24
#@Author  :    tb_youth
#@FileName:    QPushButtonDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import QPushButton,QApplication,QDialog,QVBoxLayout
from PyQt5.QtGui import QIcon,QPixmap
class PushButtonDemo(QDialog):
    def __init__(self):
        super(PushButtonDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(400,400)
        self.setWindowTitle('PushButtonDemo')

        self.button1 = QPushButton('button1')
        #设置按钮状态可拨动（切换）
        self.button1.setCheckable(True)
        # self.button1.toggle()


        self.button1.clicked.connect(lambda: self.onClickButton(self.button1))
        self.button1.clicked.connect(self.buttonStatus)

        self.button2 = QPushButton()
        self.button2.setText('图像按钮')
        #按钮前加图标
        self.button2.setIcon(QIcon(QPixmap('D:\Learn-python-notes\projects\demo\icon\统计分析.png')))
        self.button2.clicked.connect(lambda: self.onClickButton(self.button2))

        #按钮设置不可用
        self.button3 = QPushButton('不可用')
        self.button3.setEnabled(False)
        #按默认按钮（回车就点击），一个窗口只能有一个
        self.button4 = QPushButton('&默认按钮')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.onClickButton(self.button4))

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)

    def onClickButton(self,b):
        print(b.text())

    def buttonStatus(self):
        if self.button1.isChecked():
            self.move(200,200)
            print('被按下')
        else:
            self.move(800,500)
            print('被松开')


if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = PushButtonDemo()
    window.show()
    sys.exit(app.exec_())

