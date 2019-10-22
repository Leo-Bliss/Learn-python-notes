#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/22 0022 11:58
#@Author  :    tb_youth
#@FileName:    PrintSupport.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QTextEdit
from PyQt5 import QtGui,QtWidgets,QtPrintSupport
import sys
class PrintSupport(QMainWindow):
    def __init__(self):
        super(PrintSupport,self).__init__()
        self.resize(500,500)
        self.setWindowTitle('printer')
        #左上角坐标，长宽
        self.setGeometry(800,400,300,300)
        self.button = QPushButton('打印QTextEdit控件中的内容',self)
        self.button.setGeometry(20,20,260,30)
        self.editor = QTextEdit('默认文本',self)
        self.editor.setGeometry(20,60,260,200)
        self.button.clicked.connect(self.print)

    #如果电脑连接了打印机，会将内容当做图像打印
    def print(self):
        printer = QtPrintSupport.QPrinter()

        painter = QtGui.QPainter()
        #将绘制目标重定向到打印机
        painter.begin(printer)
        screen = self.editor.grab()
        painter.drawPixmap(10,10,screen)
        painter.end()
        print('print')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = PrintSupport()
    gui.show()
    app.exec_()




