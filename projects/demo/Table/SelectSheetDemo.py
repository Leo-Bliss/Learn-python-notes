#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/3/3 0003 23:48
#@Author  :    tb_youth
#@FileName:    SelectSheetDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

from PyQt5.QtWidgets import QAbstractItemView,QApplication,QWidget,QLabel,QPushButton,QListWidget
from PyQt5.QtWidgets import QGridLayout,QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class SelectSheetDemo(QWidget):
    def __init__(self, sheet_names):
        super().__init__()
        self.initUI(sheet_names)

    def initUI(self, sheet_names):
        self.setWindowTitle('选择工作表')
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setMaximumSize(425, 500)
        self.setMinimumSize(425, 500)
        self.listWidget = QListWidget()
        self.listWidget.addItems(sheet_names)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.label = QLabel('请选择excel中的工作表:')
        self.ok_button = QPushButton('确定')
        self.cancel_button = QPushButton('取消')
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.listWidget, 0, 1, 3, 3)
        gridLayout.addWidget(self.ok_button, 0, 4)
        gridLayout.addWidget(self.cancel_button, 1, 4)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.label)
        vlayout.addLayout(gridLayout)
        vlayout.setStretch(0, 1)
        vlayout.setStretch(1, 10)
        self.setLayout(vlayout)

        self.ok_button.clicked.connect(self.onClickedOK)
        self.cancel_button.clicked.connect(self.onClickedCancel)

    def onClickedOK(self):
        item = self.listWidget.selectedItems()[0]
        print(item.text())

    def onClickedCancel(self):
        self.close()


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = SelectSheetDemo(['sheet1','sheet2'])
    window.show()
    sys.exit(app.exec_())