#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/8 0008 10:54
#@Author  :    tb_youth
#@FileName:    LoadGif.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *

class LaodGifDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('装载GIF动画')
        self.label = QLabel("", self)
        self.setFixedSize(500, 500)
        self.label.resize(500, 200)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.movie = QMovie('./images/1.gif')
        self.label.setMovie(self.movie)
        self.movie.start()





if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = LaodGifDemo()
    window.show()
    sys.exit(app.exec_())

