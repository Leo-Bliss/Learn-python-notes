#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/8 0008 14:41
#@Author  :    tb_youth
#@FileName:    AnimationWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
窗口大小变化动画
QPropertyAnimation
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import  sys

class AnimationWindow(QWidget):
    def __init__(self):
        super(AnimationWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint|Qt.MSWindowsFixedSizeDialogHint)
        self.OrigHeight = 50
        self.ChangeHeight = 150
        self.setGeometry(QRect(500,400,150,self.OrigHeight))
        self.btn = QPushButton('展开',self)
        self.btn.setGeometry(10,10,60,35)
        self.btn.clicked.connect(self.onClickedChange)

    def onClickedChange(self):
        currentHeight = self.height()
        if self.OrigHeight == currentHeight:
            startHeight = self.OrigHeight
            endHeight = self.ChangeHeight
            self.btn.setText("收缩")
        else:
            startHeight = self.ChangeHeight
            endHeight = self.OrigHeight
            self.btn.setText("展开")

        self.animation = QPropertyAnimation(self,b'geometry')
        #Duration:持续时间
        self.animation.setDuration(500)
        self.animation.setStartValue(QRect(500,400,150,startHeight))
        self.animation.setEndValue(QRect(500, 400, 150, endHeight))
        self.animation.start()




if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    sys.exit(app.exec_())
