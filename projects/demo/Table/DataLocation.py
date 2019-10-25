#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/25 0025 20:46
#@Author  :    tb_youth
#@FileName:    DataLocation.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
表格中快速定位
1.数据的定位：findItems
2.找到满足条件的单元格，
会定位到单元格的所在行：setSliderPosition(row)
'''

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidget,QWidget,QHBoxLayout,QTableWidgetItem
from PyQt5 import QtCore
from PyQt5.QtGui import QColor,QBrush

class DataLocationDemo(QWidget):
    def __init__(self):
        super(DataLocationDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(600,600)
        self.setWindowTitle('DataLocation')
        #创建
        tableWidget = QTableWidget()
        tableWidget.setRowCount(40)
        tableWidget.setColumnCount(4)
       #设置数据
        for i in range(40):
            for j in range(4):
                content = '(%d %d)'%(i,j)
                tableWidget.setItem(i,j,QTableWidgetItem(content))
        #布局
        layout = QHBoxLayout()
        layout.addWidget(tableWidget)
        self.setLayout(layout)

        # #搜索所有满足条件的项
        # text = '(13 1)'
        # items = tableWidget.findItems(text,QtCore.Qt.MatchExactly)
        #搜索第一个满足的
        text = '(10'
        items = tableWidget.findItems(text,QtCore.Qt.MatchStartsWith)
        if len(items) > 0:
            item = items[0]
            item.setBackground(QColor(0,255,0))
            item.setForeground(QColor(255,0,0))

            row = item.row()
            #定位到行
            tableWidget.verticalScrollBar().setSliderPosition(row)
        else:
            print('没有满足条件的项')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataLocationDemo()
    window.show()
    sys.exit(app.exec_())


