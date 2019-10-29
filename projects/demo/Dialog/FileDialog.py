#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/23 0023 23:08
#@Author  :    tb_youth
#@FileName:    FileDialog.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
QFileDialog
打开图像文件，文本文件，显示到窗口
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QtCore import *

class FileDialogDemo(QWidget):
    def __init__(self):
        super(FileDialogDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('FileDialogDemo')

        self.button1 = QPushButton('打开图片')
        self.image_label = QLabel()
        self.button2 = QPushButton('打开文本')
        self.content = QTextEdit()

        #控件垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.image_label)
        layout.addWidget(self.button2)
        layout.addWidget(self.content)
        self.setLayout(layout)

        #

        #添加相关信号
        self.button1.clicked.connect(self.loadImage)
        self.button2.clicked.connect(self.loadFile)

    def loadImage(self):
        fname,_ = QFileDialog.getOpenFileName(self,'打开图片','.','图像文件(*.png *.jpg)')
        self.image_label.setPixmap(QPixmap(fname))

    def loadFile(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec_():
            file_name = dialog.selectedFiles()
            f = open(file_name[0],encoding='utf-8',mode='r')
            with f:
                data = f.read()
                self.content.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileDialogDemo()
    window.show()
    sys.exit(app.exec_())


