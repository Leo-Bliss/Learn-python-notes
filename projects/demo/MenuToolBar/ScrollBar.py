#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/3/1 0001 23:15
#@Author  :    tb_youth
#@FileName:    ScrollBar.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
滚动条控件（QScrollBar）
作用：
1.通过滚动条值的变化控制其他控件的状态变化
（比如，通过滚动条来修改label的字体颜色）
2.通过滚动条的位置控制控件的位置变化
'''
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QScrollBar
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import QPalette,QColor
import sys

class ScrollBarDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.label = QLabel("通过滚动条改变字体颜色")
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.label)

        self.scrollbar1 = QScrollBar()
        self.scrollbar1.setMaximum(255)
        self.scrollbar1.sliderMoved.connect(self.sliderMoved)

        self.scrollbar2 = QScrollBar()
        self.scrollbar2.setMaximum(255)
        self.scrollbar2.sliderMoved.connect(self.sliderMoved)

        self.scrollbar3 = QScrollBar()
        self.scrollbar3.setMaximum(255)
        self.scrollbar3.sliderMoved.connect(self.sliderMoved)

        self.scrollbar4= QScrollBar()
        self.scrollbar4.setMaximum(255)
        self.scrollbar4.sliderMoved.connect(self.sliderMoved1)

        hlayout.addWidget(self.scrollbar1)
        hlayout.addWidget(self.scrollbar2)
        hlayout.addWidget(self.scrollbar3)
        hlayout.addWidget(self.scrollbar4)

        self.setLayout(hlayout)

        self.y = self.label.pos().y()

    def sliderMoved(self):
        print(self.scrollbar1.value(),self.scrollbar2.value(),self.scrollbar3.value())
        palette = QPalette()
        color = QColor(self.scrollbar1.value(),self.scrollbar2.value(),self.scrollbar3.value(),255)
        palette.setColor(QPalette.Foreground,color)
        self.label.setPalette(palette)

    def sliderMoved1(self):
        self.label.move(self.label.x(),self.y+self.scrollbar4.value())




if __name__=='__main__':
    app = QApplication(sys.argv)
    window = ScrollBarDemo()
    window.show()
    sys.exit(app.exec_())