#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/25 0025 20:21
#@Author  :    tb_youth
#@FileName:    PlaceControlCell.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import *
class PlaceControlIntoCellDemo(QWidget):
    def __init__(self):
        super(PlaceControlIntoCellDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('表格中放入控件')
        #创建
        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)
        tablewidget.setHorizontalHeaderLabels(['name','job','other'])
        text_item = QTableWidgetItem('Bob')
        tablewidget.setItem(0,0,text_item)

        #combox
        combox = QComboBox()
        combox.addItem('Teacher')
        combox.addItem('Student')
        #QCSS
        combox.setStyleSheet('QComboBox{margin:3px};')
        tablewidget.setCellWidget(0,1,combox)
        button = QPushButton('ok')
        #已经被按下
        button.setDown(True)
        #QCsS
        button.setStyleSheet('QPushButton{margin:3px};')
        tablewidget.setCellWidget(0,2,button)
        #布局
        layout = QHBoxLayout()
        layout.addWidget(tablewidget)
        self.setLayout(layout)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = PlaceControlIntoCellDemo()
    window.show()
    sys.exit(app.exec_())



