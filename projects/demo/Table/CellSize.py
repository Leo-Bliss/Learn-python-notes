#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/25 0025 21:20
#@Author  :    tb_youth
#@FileName:    CellSize.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
单元格大小:setRowHeight(row,size) setColumnWidth(col,size)
单元格合并:setSpan(x,y,rowSpan,colSpan)
'''
import sys
from PyQt5.QtWidgets import QApplication,QTableWidgetItem,QWidget,QTableWidget,QHBoxLayout

class CellSizeDemo(QWidget):
    def __init__(self):
        super(CellSizeDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('setCellSize')

        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        tableWidget.setHorizontalHeaderLabels(['A','B','C'])

        item1 = 'Hello, I xxxxxxxxxxxxxxxxxxxxxxxx.Thank you!'
        tableWidget.setItem(0,0,QTableWidgetItem(item1))

        tableWidget.setItem(2, 0, QTableWidgetItem("Joe"))
        tableWidget.setSpan(2,0,2,1)

        #修改表格大小
        #第一个参数：row
        tableWidget.setRowHeight(0,80)
        # 第一个参数：column
        tableWidget.setColumnWidth(0,300)


        layout = QHBoxLayout()
        layout.addWidget(tableWidget)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CellSizeDemo()
    window.show()
    sys.exit(app.exec_())

