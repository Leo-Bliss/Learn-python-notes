#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/9 0009 22:42
#@Author  :    tb_youth
#@FileName:    DataGrid.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
使用可视化方式对SQLite数据库进行增删改查

QtableView
QSqlTableMOdel

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

def  initModel(model):
    model.setTable('user')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0,Qt.Horizontal,'ID')
    model.setHeaderData(1, Qt.Horizontal, 'name')
    model.setHeaderData(2, Qt.Horizontal, 'age')
    model.setHeaderData(3, Qt.Horizontal, 'address')
    model.setHeaderData(4, Qt.Horizontal, 'tel')

def createView(title,model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def findrow(i):
    delrow = i.row()
    print('row=%s'%str(delrow))

#增加完数据向上单击即可添加入数据库
def addrow():
    #当前行的下方添加一行
    ret = model.insertRows(view.currentIndex().row()+1,1)
    print('insertRow=%s'%str(ret))



if __name__=='__main__':
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/database.db')
    model = QSqlTableModel()
    delrow = -1
    initModel(model)
    view = createView('show',model)
    view.clicked.connect(findrow)

    dlg = QDialog()
    layout = QVBoxLayout()
    layout.addWidget(view)
    addBtn = QPushButton('添加一行')
    delBtn = QPushButton('删除一行')
    addBtn.clicked.connect(addrow)
    delBtn.clicked.connect(lambda: model.removeRow(view.currentIndex().row()))

    layout.addWidget(addBtn)
    layout.addWidget(delBtn)
    dlg.setWindowTitle('Database View')
    dlg.resize(700,500)
    dlg.setLayout(layout)
    dlg.show()
    sys.exit(app.exec_())
