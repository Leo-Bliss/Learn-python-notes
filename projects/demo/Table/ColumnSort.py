#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/3/2 0002 22:24
#@Author  :    tb_youth
#@FileName:    ColumnSort.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
表格按列排序：
1. 按哪列排序
2. 排序类型：升序或降序
sortItem（columnIndex，orderType）
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QTableWidget,QTableWidgetItem
from PyQt5.QtWidgets import QVBoxLayout,QPushButton
from PyQt5.QtCore import Qt

class ColumnSortDemo(QWidget):
    def __init__(self):
        super(ColumnSortDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("按列排序")
        self.resize(430,300)
        layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['name','sex','weight(kg)'])
        newItem = QTableWidgetItem('Bob')
        self.tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('male')
        self.tableWidget.setItem(0,1,newItem)

        newItem = QTableWidgetItem('50')
        newItem.setTextAlignment(Qt.AlignRight)
        self.tableWidget.setItem(0,2,newItem)

        newItem = QTableWidgetItem('Mike')
        self.tableWidget.setItem(1, 0, newItem)

        newItem = QTableWidgetItem('male')
        self.tableWidget.setItem(1, 1, newItem)

        newItem = QTableWidgetItem('55')
        newItem.setTextAlignment(Qt.AlignRight)
        self.tableWidget.setItem(1, 2, newItem)

        newItem = QTableWidgetItem('Alice')
        self.tableWidget.setItem(2, 0, newItem)

        newItem = QTableWidgetItem('female')
        self.tableWidget.setItem(2, 1, newItem)

        newItem = QTableWidgetItem('45')
        newItem.setTextAlignment(Qt.AlignRight)
        self.tableWidget.setItem(2, 2, newItem)

        newItem = QTableWidgetItem('Lily')
        self.tableWidget.setItem(3, 0, newItem)

        newItem = QTableWidgetItem('female')
        self.tableWidget.setItem(3, 1, newItem)

        newItem = QTableWidgetItem('43')
        newItem.setTextAlignment(Qt.AlignRight)
        self.tableWidget.setItem(3, 2, newItem)

        self.button = QPushButton('sort')
        self.button.clicked.connect(self.order)
        layout.addWidget(self.button)
        self.orderType = Qt.DescendingOrder
        self.setLayout(layout)

    def order(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder
        self.tableWidget.sortItems(2,self.orderType)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = ColumnSortDemo()
    window.show()
    sys.exit(app.exec_())

