#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/10 0010 22:25
#@Author  :    tb_youth
#@FileName:    QMessageBoxDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
1.关于对话框
2.错误对话框
3.警告对话框
4.提问对话框
5.消息对话框

有两点差异：
1.显示的对话框图标可能不太
2.显示的按钮是不一样的
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QPushButton,QVBoxLayout

class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('QMessageBox')

        self.button1 = QPushButton('显示关于对话框')
        self.button2 = QPushButton('显示错误对话框')
        self.button3= QPushButton('显示警告对话框')
        self.button4 = QPushButton('显示提问对话框')
        self.button5 = QPushButton('显示消息对话框')


        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)

        self.setLayout(layout)

        self.button1.clicked.connect(self.showDialog)
        self.button2.clicked.connect(self.showDialog)
        self.button3.clicked.connect(self.showDialog)
        self.button4.clicked.connect(self.showDialog)
        self.button5.clicked.connect(self.showDialog)

    def showDialog(self):
       text = self.sender().text()
       if(text == '显示关于对话框'):
           QMessageBox.about(self, '关于','关于对话框')
       elif(text == '显示错误对话框'):
           QMessageBox.critical(self,'错误','错误对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
       elif (text == '显示警告对话框'):
           QMessageBox.warning(self,'警告', '警告对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
       elif (text == '显示提问对话框'):
           QMessageBox.question(self,'提问', '提问对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
       else:
           QMessageBox.information(self,'消息','消息对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = QMessageBoxDemo()
    window.show()
    sys.exit(app.exec_())