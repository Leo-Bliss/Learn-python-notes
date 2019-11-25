#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/22 0022 13:01
#@Author  :    tb_youth
#@FileName:    TableView.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
显示二维表数据（QtableView）
数据源

Model
需要创建QTableView实例
和一个数据源（Model），然后两者进行关联
MVC: M-->Model,V-->Viewer C--->Controller
MVC的目的是使后端数据与前端页面耦合度降低
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
class TableView(QWidget):
    def __init__(self):
        super(TableView,self).__init__()
        self.setWindowTitle('TableViewDemo')
        self.resize(800,400)
        #row colum
        self.model = QStandardItemModel(15,6)
        #设置表头（水平表头）
        self.model.setHorizontalHeaderLabels(['id','name','age'])

        self.tableview = QTableView()
        #关联model
        self.tableview.setModel(self.model)
        #添加数据
        item11 = QStandardItem('201701014011')
        item12 = QStandardItem('tb_youth')
        item13 = QStandardItem('21')
        self.model.setItem(0,0,item11)
        self.model.setItem(0,1,item12)
        self.model.setItem(0,2,item13)
        # self.model.appendRow([QStandardItem('1'),QStandardItem('2'),QStandardItem('3')])
        #不可编辑
        # self.tableview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #布局
        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = TableView()
    window.show()
    sys.exit(app.exec_())

