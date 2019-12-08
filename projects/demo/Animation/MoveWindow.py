#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/8 0008 15:17
#@Author  :    tb_youth
#@FileName:    MoveWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import  sys

def paralleMove():
    app = QApplication(sys.argv)
    window1 = QMainWindow()
    window1.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
    window1.show()
    window2 = QMainWindow()
    window2.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
    window2.show()

    animation1 = QPropertyAnimation(window1, b'geometry')
    animation2 = QPropertyAnimation(window2, b'geometry')

    group = QParallelAnimationGroup()
    group.addAnimation(animation1)
    group.addAnimation(animation2)

    animation1.setDuration(3000)
    animation1.setStartValue(QRect(0, 0, 100, 30))
    animation1.setEndValue(QRect(250, 250, 100, 30))
    # 动画特效:Easing Curve-->缓和曲线
    animation1.setEasingCurve(QEasingCurve.OutBack)

    animation2.setDuration(3000)
    animation2.setStartValue(QRect(0, 0, 160, 30))
    animation2.setEndValue(QRect(750, 250, 100, 30))
    animation2.setEasingCurve(QEasingCurve.CosineCurve)

    group.start()
    sys.exit(app.exec_())




if __name__ =='__main__':
    paralleMove()
