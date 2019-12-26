#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    17:13  2019/12/26
#@Author  :    tb_youth
#@FileName:    HomeWindow.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QHBoxLayout
from PyQt5.QtGui import QPainter,QPalette,QPixmap,QBrush

class HomeWindow(QWidget):
    def __init__(self):
        super(HomeWindow,self).__init__()
        self.resize(1000,800)


        # # 背景图片
        # palette = QPalette()
        # pix = QPixmap('./image/page1.png')
        # pix.scaled(self.width(),self.height())
        # palette.setBrush(QPalette.Background,QBrush(pix))
        # self.setPalette(palette)

        # self.label = QLabel()
        # self.label.setStyleSheet('QLabel{border-image:url( ./image/page2.png);}')
        # layout = QHBoxLayout()
        # layout.addWidget(self.label)
        # self.setLayout(layout)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        # todo 设置背景图片，平铺到整个窗口，随着窗口改变而改变
        pixmap = QPixmap('./image/page1.png')
        painter.drawPixmap(self.rect(), pixmap)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec_())
