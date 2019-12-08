#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/8 0008 13:32
#@Author  :    tb_youth
#@FileName:    ScaleImage.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import Qt

class ScaleImageDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('图片大小缩放')
        file_name = './images/1.png'
        img = QImage(file_name)
        label = QLabel(self)
        label.setFixedSize(50,50)

        #IgnoreAspectRatio:忽略等比例，SmoothTransformation：图片尽量平滑
        result = img.scaled(label.width(),label.height(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        label.setPixmap(QPixmap.fromImage(result))

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        self.setLayout(vbox)



if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = ScaleImageDemo()
    window.show()
    sys.exit(app.exec_())
