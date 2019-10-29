#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/25 0025 14:46
#@Author  :    tb_youth
#@FileName:    TableWidget.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import  sys
# from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QWidget,QTableWidget,QTableWidgetItem
from PyQt5.QtWidgets import *

class TableWidget(QWidget):
    def __init__(self):
        super(TableWidget,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('TableWidgetDemo')
        #表格窗口
        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)

        #增加数据
        tablewidget.setHorizontalHeaderLabels(['id','name','class'])
        item = QTableWidgetItem('201701014011')
        tablewidget.setItem(0,0,item)


        #设置不可编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #整行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        #大小根据内容调整
        tablewidget.resizeRowsToContents()
        tablewidget.resizeColumnsToContents()
        # #设置表头隐藏:没有这个方法？？？
        # tablewidget.horizontalHeader().setVishible(False)
        # tablewidget.verticalHeader().setVisible(False)
        #设置头部标签
        tablewidget.setVerticalHeaderLabels(['a','b','c'])
        #隐藏表格线
        tablewidget.setShowGrid(False)
        # 布局
        layout = QHBoxLayout()
        layout.addWidget(tablewidget)
        self.setLayout(layout)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = TableWidget()
    window.show()
    sys.exit(app.exec_())



