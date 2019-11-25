#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/25 0025 22:41
#@Author  :    tb_youth
#@FileName:    InputWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
导入数据界面：
支持数据预处理，数据查找
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QTabWidget
from PyQt5.QtWidgets import QTableWidget,QTableView
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QStandardItemModel

class InputWindowDemo(QTabWidget):
    def __init__(self):
        super(InputWindowDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500,100,1000,900)

        #创建两个窗口
        #tab1：显示全部，tab2：只显示变量
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.addTab(self.tab1,'数据视图')
        self.addTab(self.tab2,'变量视图')

        #tab放在底部
        self.setTabPosition(QTabWidget.TabPosition.South)
        #tab形状：设置为三角形：Triangular，圆角为：Rouned
        self.setTabShape(QTabWidget.Triangular)

        #添加表格
        self.mode = QStandardItemModel(100, 15000)
        self.initTab1()
        self.initTab2()

    def initTab1(self):
        self.tableview1 = QTableView()
        self.tableview1.setModel(self.mode)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.tableview1)
        self.tab1.setLayout(vlayout)

    def initTab2(self):
        self.tableview2 = QTableView()
        self.tableview2.setModel(self.mode)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.tableview2)
        self.tab2.setLayout(vlayout)

    def loadData(self):
        pass







if __name__=='__main__':
    app = QApplication(sys.argv)
    window = InputWindowDemo()
    window.show()
    sys.exit(app.exec_())