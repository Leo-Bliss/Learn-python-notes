#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    :    2020/1/5 0005 0:41
# @Author  :    tb_youth
# @FileName:    FramelessWindow.py
# @SoftWare:    PyCharm
# @Blog    :    https://blog.csdn.net/tb_youth

'''
无边框窗口：
窗口移动
右上角窗口操作：
最小化，最大化，关闭，还原窗口大小
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QAction, QToolBar
from PyQt5.QtGui import QBitmap, QPainter, QPixmap, QCursor
from PyQt5.QtCore import Qt


class FrameLessWindow(QWidget):
    def __init__(self):
        super(FrameLessWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("异形窗口")
        self.pix = QBitmap('./image/mask2.png')
        self.resize(self.pix.size())
        self.initPos = self.pos()
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.tool_bar = QToolBar()
        self.normal_action = QAction('#')
        self.normal_action.setToolTip('还原')
        self.min_action = QAction("-")
        self.min_action.setToolTip('最小化')
        self.max_action = QAction("+")
        self.max_action.setToolTip('最大化')
        self.close_action = QAction("x")
        self.close_action.setToolTip('关闭')

        self.tool_bar.addAction(self.normal_action)
        self.tool_bar.addAction(self.min_action)
        self.tool_bar.addAction(self.max_action)
        self.tool_bar.addAction(self.close_action)

        self.min_button = QPushButton("最小")
        self.max_normal_button = QPushButton("最大")
        self.close_button = QPushButton("关闭")
        self.max_normal_button.setCheckable(True)
        self.max_normal_button.setDefault(False)


        # 通过水平布局和垂直布局将action设置在右上角
        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(self.tool_bar)
        # hlayout.addWidget(self.min_button)
        # hlayout.addWidget(self.max_normal_button)
        # hlayout.addWidget(self.close_button)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addStretch(1)
        self.setLayout(vlayout)

        self.min_button.clicked.connect(self.showMinWindow)
        self.max_normal_button.clicked.connect(self.showMaxNormalWindow)
        self.close_button.clicked.connect(self.closeWindow)

        self.normal_action.triggered.connect(self.showNormalWindow)
        self.close_action.triggered.connect(self.closeWindow)
        self.min_action.triggered.connect(self.showMinWindow)
        self.max_action.triggered.connect(self.showMaxWindow)



    # 设置窗口背景随窗口改变而改变
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.width(), self.height(), QPixmap('./image/screen1.jpg'))

    # 鼠标按下事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 鼠标左键按下，开始拖动
            self.m_drag = True

            # 按下点相对屏幕的坐标
            print(event.globalPos())
            # 按下点相对窗口坐标，不包含标题栏
            print(event.pos())
            # 窗口左上角坐标
            print(self.pos())

            # 按下点相对窗口坐标，包含标题栏
            self.m_drapPosition = event.globalPos() - self.pos()
            # 光标样式
            self.setCursor(QCursor(Qt.OpenHandCursor))


    def mouseMoveEvent(self, event):
        # 实时计算窗口左上角坐标(要减去包含标题栏的坐标)
        self.move(event.globalPos() - self.m_drapPosition)

    def mouseReleaseEvent(self, event):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def closeWindow(self):
        self.close()

    def showMinWindow(self):
        self.showMinimized()

    def showMaxNormalWindow(self):
        print(self.max_normal_button.isChecked())
        if self.max_normal_button.isChecked():
            self.showMaximized()
        else:
            self.showNormal()

    def showMaxWindow(self):
        self.showMaximized()

    def showNormalWindow(self):
        self.showNormal()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FrameLessWindow()
    window.show()
    sys.exit(app.exec_())
