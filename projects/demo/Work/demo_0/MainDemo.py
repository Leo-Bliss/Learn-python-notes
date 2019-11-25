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
    def __init__(self):
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

class AboutDialog(QDialog):
    def __init__(self):
        super(AboutDialog,self).__init__()
        self.initUI()
    def initUI(self):
        pass


class Demo(QMainWindow):
    def __init__(self):
        super(Demo,self).__init__()
        self.initUI()
    def initUI(self):
        path = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Learn-python-notes\projects\demo\icon'
        self.setWindowIcon(QIcon(path+'\分析.png'))
        self.setWindowTitle('Demo')
        #坐标，大小
        self.setGeometry(500,100,1000,900)

        #toolbar
        toolbar1 = self.addToolBar('File')

        new = QAction(QIcon(path+'\新建.png'),'new',self)
        open = QAction(QIcon(path+'\打开.png'),'open',self)
        save = QAction(QIcon(path+'\保存.png'),'save',self)
        search = QAction(QIcon(path+'\搜索.png'), 'search', self)
        setting = QAction(QIcon(path+'\参数.png'), 'setting', self)
        run = QAction(QIcon(path+'\运行.png'), 'run', self)
        toolbar1.addAction(new)
        toolbar1.addAction(open)
        toolbar1.addAction(save)
        toolbar1.addAction(search)

        toolbar2 = self.addToolBar('Setting')
        toolbar2.addAction(setting)
        toolbar2.addAction(run)

        # toolbar2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toolbar1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        #绑定事件
        open.triggered.connect(self.clickOpen)
        new.triggered.connect(self.clickCreate)
        save.triggered.connect(self.clickSave)
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

        #菜单栏
        bar = self.menuBar()
        #主菜单
        file = bar.addMenu('File')
        #子菜单
        new = file.addAction('new')
        open = file.addAction('open')
        save = file.addAction('save')
        exit = file.addAction('exit')

        edit = bar.addMenu('Edit')
        cut = edit.addAction('cut')
        copy = edit.addAction('copy')
        paste = edit.addAction('paste')
        delete = edit.addAction('delete')

        model = bar.addMenu('Model')
        run = bar.addMenu('Run')
        help = bar.addMenu('Help')
        about = help.addAction('about')

        # # 背景图片
        # palette1 = QPalette()
        # pix = QPixmap('./flower.jpg')
        # pix = pix.scaled(1000, 900)
        # palette1.setBrush(QPalette.Background, QBrush(pix))
        # self.setPalette(palette1)

    def clickOpen(self):
        self.status.showMessage('打开文件',5000)
        # # self.file = QFileDialog.getOpenFileName(self,'打开文件','C:\\Users\Administrator\AppData\Local\Programs\Python\Python37\Learn-python-notes')
        # print(self.file)
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.AnyFile)
        dir = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Learn-python-notes'
        self.dialog.setDirectory(dir)
        self.dialog.setFilter(QDir.Files)
        if self.dialog.exec_():
            try:
                file_name = self.dialog.selectedFiles()[0]
                #print(file_name)
                # read_excel_xlsx(self,file_name,'Sheet1')
                read_xlsx(self,file_name)
            except Exception as e:
                pass

    def clickCreate(self):
        self.mode = QStandardItemModel(100,15000)
        self.tableview.setModel(self.mode)

    def searchData(self):
        self.dialog = SearchDialog()
        self.dialog.show()

    def clickSave(self):
        file_path,self.save = QFileDialog.getSaveFileName(self,'保存文件','C:/',
                                                          'ALL Files(*);;xlsx(*.xlsx);;xls(*.xls);;csv(*.csv);;txt(*.txt)')
        # print(file_path)
        #文件中写入数据
        try:
            with open(file_path,'w',encoding='utf-8') as f:
                pass
        except Exception as e:
            pass





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

