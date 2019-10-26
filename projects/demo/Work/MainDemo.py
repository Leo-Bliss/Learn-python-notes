#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/24 0024 11:42
#@Author  :    tb_youth
#@FileName:    MainDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth



import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
import xlrd
from openpyxl import workbook,load_workbook


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super(TableModel, self).__init__(parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0]) if self.rowCount() else 0

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row = index.row()
            if 0 <= row < self.rowCount():
                column = index.column()
                if 0 <= column < self.columnCount():
                    return self._data[row][column]

class SearchDialog(QDialog):
    def __int__(self):
        super(SearchDialog,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 200)
        self.setWindowTitle('查找')
        self.row_label = QLabel('查找行  :')
        self.col_label = QLabel('查找列  :')
        self.row_edit = QLineEdit()
        self.col_edit = QLineEdit()
        self.txt_label = QLabel('查找内容:')
        self.txt_edit = QLineEdit()
        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(self.row_label)
        self.hbox1.addWidget(self.row_edit)
        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.col_label)
        self.hbox2.addWidget(self.col_edit)
        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(self.txt_label)
        self.hbox3.addWidget(self.txt_edit)
        self.btnOK = QPushButton('OK')
        self.btnCancel = QPushButton('Cancel')
        self.hbox4 = QHBoxLayout()
        self.hbox4.addWidget(self.btnCancel)
        self.hbox4.addWidget(self.btnOK)
        self.flayout = QFormLayout()
        self.flayout.addItem(self.hbox1)
        self.flayout.addItem(self.hbox2)
        self.flayout.addItem(self.hbox3)
        self.flayout.addItem(self.hbox4)
        self.setLayout(self.flayout)


class Demo(QMainWindow):
    def __init__(self):
        super(Demo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowIcon(QIcon('D:\Learn-python-notes\projects\demo\icon\分析.png'))
        self.setWindowTitle('Demo')
        #坐标，大小
        self.setGeometry(500,100,1000,900)

        #toolbar
        toolbar1 = self.addToolBar('File')
        new = QAction(QIcon('D:\Learn-python-notes\projects\demo\icon\新建.png'),'new',self)
        open = QAction(QIcon('D:\Learn-python-notes\projects\demo\icon\打开.png'),'open',self)
        save = QAction(QIcon('D:\Learn-python-notes\projects\demo\icon\保存.png'),'save',self)
        search = QAction(QIcon('D:\Learn-python-notes\projects\demo\icon\搜索.png'), 'search', self)
        setting = QAction(QIcon('D:\Learn-python-notes\projects\demo\icon\设置.png'), 'setting', self)

        toolbar1.addAction(new)
        toolbar1.addAction(open)
        toolbar1.addAction(save)
        toolbar1.addAction(search)

        toolbar2 = self.addToolBar('Setting')
        toolbar2.addAction(setting)
        toolbar2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        toolbar1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        #绑定事件
        open.triggered.connect(self.clickOpen)
        new.triggered.connect(self.clickCreate)
        search.triggered.connect(self.searchData)

        #表格
        self.tableview = QTableView(self)
        self.setCentralWidget(self.tableview)

        #文本框
        self.textEdit1 = QTextEdit()
        self.textEdit2 = QTextEdit()
        #状态栏
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage('欢迎使用中医药数据特征选择分析平台',5000)


        # #布局
        # self.layoutWidget = QWidget(self)
        # self.layoutWidget.setObjectName("layoutWidget")
        # #x,y,width,height
        # self.layoutWidget.setGeometry(QtCore.QRect(0, 50, 1000, 850))
        # self.gridLayout = QGridLayout(self.layoutWidget)
        # # self.tableview.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        # # self.textEdit1.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        # self.gridLayout.addWidget(self.tableview,0,0,1,1)
        # # self.gridLayout.addWidget(self.textEdit1,0,1,1,4)
        # # self.gridLayout.addWidget(self.textEdit2,0,2,1,4)

        # # 背景图片
        # palette1 = QPalette()
        # pix = QPixmap('./flower.jpg')
        # pix = pix.scaled(1000, 900)
        # palette1.setBrush(QPalette.Background, QBrush(pix))
        # self.setPalette(palette1)

    def clickOpen(self):
        self.status.showMessage('打开文件',5000)
        #self.file = QFileDialog.getOpenFileName(self,'打开文件','.')
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.AnyFile)
        self.dialog.setFilter(QDir.Files)
        if self.dialog.exec_():
            file_name = self.dialog.selectedFiles()[0]
            #print(file_name)
            # read_excel_xlsx(self,file_name,'Sheet1')
            read_xlsx(self,file_name)

    def clickCreate(self):
        self.mode = QStandardItemModel(100,15000)
        self.tableview.setModel(self.mode)

    def searchData(self):
        pass
        # self.dialog = SearchDialog()
        # self.dialog.initUI()
        # self.dialog.show()




def read_excel_xlsx(self,path, sheet_name='Sheet'):
    wb = load_workbook(path)
    sheet = wb[sheet_name]
    for i,row in enumerate(sheet.rows):
        for j,cell in enumerate(row):
            self.mode.setItem(i,j,QStandardItem(str(cell.value)))
        #     print(i,j,cell.value, "\t", end='')
        # print('')

def read_xlsx(self,path):
    timer = QElapsedTimer()
    timer.start()
    #打开文件
    workbook = xlrd.open_workbook(path)
    #获取sheet
    # sheet_name = workbook.sheet_names()[0]
    # print(sheet_name)
    sheet1 = workbook.sheet_by_index(0)
    # print('Sheet name: %s' % sheet1.name)
    # head = sheet1.row_values(0)
    # self.mode.setHorizontalHeaderLabels(list(head))
    rows = len(sheet1.col_values(0))
    self._data = [sheet1.row_values(i) for i in range(rows)]
    print('init data need %s seconds'%(timer.elapsed()/1000))
    # print(self._data)
    mode = TableModel(self._data, self.tableview)
    self.tableview.setModel(mode)
    # #根据内容调整表格
    # self.tableview.resizeRowsToContents()
    # self.tableview.resizeColumnsToContents()

    print('input data need %s seconds' % (timer.elapsed()/1000))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec_())

