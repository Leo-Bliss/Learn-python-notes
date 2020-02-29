#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/2/27 0027 22:47
#@Author  :    tb_youth
#@FileName:    showDataDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
表格数据展示：
1.可以从本地导入表格
2. 可以批量上传数据到本地数据库
3. 可以从数据库中选择表格导入
4.对于多个sheet的表格可以选择导入选择的sheet数据，
在数据库中相当于把原来一个表格多个sheet的拆分成了多个表格。
5.后期实现对展示的数据的修改：
全选，复制，粘贴，批量修改

【想法说明】：
上传数据到本地数据库的优点：
1.可以作数据备份
2.对于要经常用的数据及大数据表格可以先上传到
用户本地数据库，从本地数据库中取数据可以提高IO性能，
同时便于修改数据及数据同步。
【...】
而对于小型表格数据且用完不在需要的数据，则可以直接从本地导入数据

'''
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QTableView,QMenuBar
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QDialog,QLabel,QStyleFactory
from PyQt5.QtWidgets import QCompleter,QComboBox
from PyQt5.QtWidgets import QListWidget,QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel
from PyQt5.QtWidgets import QPushButton
# from projects.demo.Work.TCM_DSAS.localDB.src_.DBOperator import DBOperator
import sys

class MyComBox(QComboBox):
    def __init__(self,data_list):
        super().__init__()
        self.addItems(data_list)
        self.setEditable(True)
        self.completer = QCompleter(data_list)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)
        style = '''
                          background-color: #294662;
                          color: #ffffff;
                          border: 1px solid #375C80;
                          border-radius: 5px;
                          padding: 0px 0px 0px 0px;
                          min-width: 17px;
                         font: 14px "Arial";
                '''
        self.completer.popup().setStyleSheet(style)


class DBInfor(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('数据仓库')
        vlayout = QVBoxLayout()

        self.label1 = QLabel('选择仓库：')
        db_list = ['database', 'userDB', 'R']
        self.combox1 = MyComBox(db_list)
        self.label2 = QLabel('选择表格：')
        table_list = ['test1', 'test2', 'user']
        self.combox2 = MyComBox(table_list)
        self.input_button = QPushButton('导入')

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self.label1)
        hlayout1.addWidget(self.combox1)
        hlayout1.addWidget(self.label2)
        hlayout1.addWidget(self.combox2)
        hlayout1.addWidget(self.input_button)
        hlayout1.setStretch(0,1)
        hlayout1.setStretch(1,3)
        hlayout1.setStretch(2, 1)
        hlayout1.setStretch(3, 3)
        hlayout1.setStretch(4,1)
        hlayout1.setSpacing(10)
        self.list_widget = QListWidget()

        self.list_widget.addItems(table_list)
        self.list_widget.itemClicked.connect(self.onItemClicked)
        vlayout.addLayout(hlayout1)
        vlayout.addWidget(self.list_widget)


        self.setLayout(vlayout)

    def onItemClicked(self,index):
        print(index)
        table_name = self.list_widget.item(self.list_widget.row(index)).text()
        print(table_name)
        choose = QMessageBox.information(self,'表格','您选择的是：{}'.format(table_name),QMessageBox.No|QMessageBox.Yes,QMessageBox.Yes)
        if QMessageBox.Yes == choose:
            print('yes')
        else:
            print('no')


class ShowDataDemo(QWidget):
    def __init__(self):
        super(ShowDataDemo,self).__init__()
        self.initUI()
        QApplication.setStyle(QStyleFactory.keys()[2])

    def initUI(self):
        self.resize(1200,800)
        self.setWindowTitle('showDemo')

        self.menu_bar = QMenuBar()
        #addMenu return QMenu
        self.file = self.menu_bar.addMenu('File')
        self.edit = self.menu_bar.addMenu('Edit')
        self.view = self.menu_bar.addMenu('View')
        self.help = self.menu_bar.addMenu('Help')

        #child Menu add QAction
        self.input = self.file.addMenu('导入数据')
        self.open_local = self.input.addAction('本地导入')
        self.open_db = self.input.addAction('仓库导入')

        self.open_db.triggered.connect(self.triggeredOpenDB)


        self.label1 = QLabel('选择仓库：')
        db_list = [ '####','database']
        self.combox1 = MyComBox(db_list)
        self.label2 = QLabel('选择表格：')
        table_list = ['####','test1', 'test2', 'user']
        self.combox2 = MyComBox(table_list)
        self.input_button = QPushButton('导入')

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self.label1)
        hlayout1.addWidget(self.combox1)
        hlayout1.addWidget(self.label2)
        hlayout1.addWidget(self.combox2)
        hlayout1.addWidget(self.input_button)
        hlayout1.addStretch(5)
        hlayout1.setStretch(0,1)
        hlayout1.setStretch(1,3)
        hlayout1.setStretch(2, 1)
        hlayout1.setStretch(3, 3)
        hlayout1.setStretch(4,1)
        hlayout1.setSpacing(10)


        self.table_view = QTableView()
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.model = QStandardItemModel(200, 200)
        self.table_view.setModel(self.model)
        # self.initCombox()


        self.combox1.currentIndexChanged.connect(self.selectChanged)
        self.input_button.clicked.connect(self.inputTable)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.menu_bar)
        vlayout.addLayout(hlayout1)
        vlayout.addWidget(self.table_view)
        self.setLayout(vlayout)

    def initCombox(self):
        db_name = 'database'
        path = r'./db/{}.db'.format(db_name)
        self.db.setDatabaseName(path)
        ok = self.db.open()
        if not ok:
            return
        self.model = QSqlTableModel()
        tb_name = 'test1'
        self.model.setTable(tb_name)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.table_view.setModel(self.model)
        # db.close()

    def resetModel(self,model):
        self.model = model
        self.table_view.setModel(self.model)

    def triggeredOpenLocal(self):
        pass

    def triggeredOpenDB(self):
        self.db_dialog = DBInfor()
        #打开数据仓库模态对话框
        self.db_dialog.exec_()

    def selectChanged(self):
        db_name = self.combox1.currentText()
        print(db_name)
        path = r'./db/{}.db'.format(db_name)
        print(path)
        # sql = 'select * from user'
        # try:
        #     operator = DBOperator(path)
        #     table_list = operator.query(sql)
        #     print(table_list)
        # except Exception as e:
        #     print(e)


    def inputTable(self):
        db_name = self.combox1.currentText()
        tb_name = self.combox2.currentText()
        print(db_name,tb_name)
        path = r'./db/{}.db'.format(db_name)
        # 初始化的数据库连接关闭
        self.db.close()
        self.db.setDatabaseName(path)
        # 新的数据库连接开启
        ok = self.db.open()
        if not ok:
            return
        self.model = QSqlTableModel()
        self.model.setTable(tb_name)
        # 可编辑策略，能编辑的时间内不能关闭数据库
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.table_view.setModel(self.model)





if __name__== '__main__':
    app = QApplication(sys.argv)
    window = ShowDataDemo()
    window.show()
    sys.exit(app.exec_())
