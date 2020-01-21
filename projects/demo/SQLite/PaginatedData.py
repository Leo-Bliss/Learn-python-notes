#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/1/18 0018 22:21
#@Author  :    tb_youth
#@FileName:    PaginatedData.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
分页显示数据
SQLite和MySQL中的 limit n,m
n:起始，往后m
limit 10,20
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QStyleFactory
from PyQt5.QtWidgets import QPushButton,QLineEdit,QLabel,QTableView,QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtSql import *
import sqlite3
import math

class PaginatedDemo(QWidget):
    def initDB(self):
        self.db_name = r'./db/database.db'
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        # 关联数据库
        self.db.setDatabaseName(self.db_name)
        # 判断是否打开
        if not self.db.open():
            print('无法打开数据库')

    def __init__(self):
        super(QWidget,self).__init__()
        self.initDB()
        # 当前页
        self.currentPage = 1
        # 总页数
        self.totalPage = 0
        self.totalRecordCount = 0
        # 每页显示记录数
        self.pageRecordCount = 15
        self.initUI()

    def initUI(self):
        self.setWindowTitle('分页显示数据')
        self.resize(800, 660)
        # 窗体风格
        QApplication.setStyle(QStyleFactory.keys()[-1])
        # 操作布局
        hlayout = QHBoxLayout()
        self.lastPage = QPushButton('前一页')
        self.nextPage = QPushButton('后一页')
        self.label1 = QLabel('转到第')
        self.lineEdit = QLineEdit()
        self.label2 = QLabel('页')
        self.go = QPushButton('Go')
        hlayout.addWidget(self.lastPage)
        hlayout.addWidget(self.nextPage)

        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(self.label1)
        hlayout2.addWidget(self.lineEdit)
        hlayout2.addWidget(self.label2)
        hlayout2.setStretch(0, 1)
        hlayout2.setStretch(1, 3)
        hlayout2.setStretch(2, 1)

        hlayout.addLayout(hlayout2)
        hlayout.addWidget(self.go)
        hlayout.addStretch()
        hlayout.setSpacing(10)

        hlayout.setStretch(0, 2)
        hlayout.setStretch(1, 2)
        hlayout.setStretch(2, 3)
        hlayout.setStretch(3, 1)
        hlayout.setStretch(4, 8)

        # 表格
        self.tableview = QTableView()
        # 表格宽度自适应调整
        self.tableview.horizontalHeader().setStretchLastSection(True)
        self.tableview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 数据model,QSqlQueryModel数据视图，是只读模式（不可修改）
        self.queryModel = QSqlQueryModel(self)
        # 设置表头
        self.queryModel.setHeaderData(0, Qt.Horizontal, 'ID')
        self.queryModel.setHeaderData(1, Qt.Horizontal, 'name')
        self.queryModel.setHeaderData(2, Qt.Horizontal, 'age')
        self.queryModel.setHeaderData(3, Qt.Horizontal, 'address')
        self.queryModel.setHeaderData(4, Qt.Horizontal, 'tel')

        # 状态布局
        hlayout3 = QHBoxLayout()
        self.total_page_label = QLabel("总共0页")
        self.current_page_pos_label = QLabel("当前第0页")
        self.total_record_label = QLabel("总共0条记录")
        hlayout3.addWidget(self.total_page_label)
        hlayout3.addWidget(self.current_page_pos_label)
        hlayout3.addWidget(self.total_record_label)

        # 总布局
        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.tableview)
        vlayout.addLayout(hlayout3)
        self.setLayout(vlayout)

        self.initStatus()
        self.recordQuery(0)
        self.tableview.setModel(self.queryModel)

        self.nextPage.clicked.connect(self.onClickedNextPage)
        self.lastPage.clicked.connect(self.onClickedLastPage)
        self.go.clicked.connect(self.onClickedGo)


    # def initData(self):
    #     #插入数据
    #     sql = "insert into user values (?,?,?,?,?)"
    #     for i in range(1,501,1):
    #         para = (i,'Ac',22,'dffd','10086')
    #         self.updateDB(sql,para)

    def updateDB(self, sql, *args):
        conn = sqlite3.connect(self.db_name, detect_types=sqlite3.PARSE_DECLTYPES)
        cursor = conn.cursor()
        try:
            cursor.execute(sql, *args)
        except Exception as e:
            #print(e)
            pass
        conn.commit()
        conn.close()

    def recordQuery(self,limitIndex):
        sql = "select * from user limit %d,%d"%(limitIndex,self.pageRecordCount)
        self.queryModel.setQuery(sql)
        # print(self.queryModel.rowCount())

    def getTotalRecordCount(self):
        sql = "select * from user"
        self.queryModel.setQuery(sql)
        #默认最多只能获取256条记录，当记录数超过256时，要强制获取更多
        while self.queryModel.canFetchMore():
            self.queryModel.fetchMore()
        return self.queryModel.rowCount()

    def initStatus(self):
        self.totalRecordCount = self.getTotalRecordCount()
        self.total_record_label.setText("总共{}条记录".format(self.totalRecordCount))
        self.totalPage = math.ceil(self.totalRecordCount/self.pageRecordCount)
        self.total_page_label.setText("总共{}页".format(self.totalPage))
        self.current_page_pos_label.setText("当前第{}页".format(1))

    def updateStatus(self):
        self.current_page_pos_label.setText("当前第{}页".format(self.currentPage))

    def onClickedNextPage(self):
        limitIndex = self.currentPage * self.pageRecordCount
        if self.totalPage and self.currentPage >= self.totalPage:
            return
        self.recordQuery(limitIndex)
        self.currentPage += 1
        self.updateStatus()

    def onClickedLastPage(self):
        limitIndex = (self.currentPage - 2) * self.pageRecordCount
        if self.currentPage == 1:
            return
        self.recordQuery(limitIndex)
        self.currentPage -= 1
        self.updateStatus()

    def onClickedGo(self):
        s = self.lineEdit.text()
        if s == '':
            return
        page = int(s)
        if page > self.totalPage or page < 1:
            return
        limitIndex = (page - 1) * self.pageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage = page
        self.updateStatus()



    #重载
    def closeEvent(self, event):
        # 关闭数据库
        self.db.close()










if __name__=='__main__':
    app = QApplication(sys.argv)
    window = PaginatedDemo()
    window.show()
    sys.exit(app.exec_())