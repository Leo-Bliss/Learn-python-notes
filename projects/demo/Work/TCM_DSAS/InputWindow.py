#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/25 0025 22:41
#@Author  :    tb_youth
#@FileName:    InputWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
导入数据界面：
支持数据预处理，数据查找
后期优化：动态加载数据，提升导入效率,设置加载数据进度条
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QTabWidget
from PyQt5.QtWidgets import QTableView,QFileDialog,QHeaderView
from PyQt5.QtWidgets import QMenuBar,QToolBar,QStatusBar
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QStandardItemModel,QPixmap,QIcon,QStandardItem
from PyQt5.QtCore import Qt,QDir,QElapsedTimer,QAbstractTableModel
import xlrd
from projects.demo.SignalSlot.CustomSignal1 import MyTypeSignal


global_data = None

class TableModel(QAbstractTableModel):
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

class WidgetDemo(QWidget):
    def __init__(self,mode):
        super(WidgetDemo,self).__init__()
        self.mode = mode
        self.initUI(mode)

    def initUI(self,mode):
        self.resize(800,800)
        self.data = None
        #菜单栏
        self.menu = QMenuBar()
        self.file = self.menu.addMenu('文件')
        self.edit = self.menu.addMenu('编辑')
        self.view = self.menu.addMenu('视图')
        self.help = self.menu.addMenu('帮助')
        #各菜单下的子菜单

        #文件菜单下的子菜单
        self.new = self.file.addAction('新建')
        self.open = self.file.addAction('打开')
        self.save = self.file.addAction('保存')
        self.save_as = self.file.addAction('另存为')

        #编辑菜单下的子菜单
        self.cut = self.edit.addAction('剪切')
        self.copy = self.edit.addAction('复制')
        self.paste = self.edit.addAction('粘贴')
        self.delete = self.edit.addAction('删除')
        self.find = self.edit.addAction('查找')
        # self.replace = self.find.addAction('替换')
        self.replace = self.edit.addAction('替换')

        #视图菜单下的子菜单
        self.view_tool_bar = self.view.addAction('工具栏')
        self.view_status_bar = self.view.addAction('状态栏')

        #帮助菜单下的子菜单
        self.about = self.help.addAction('关于')

        #工具栏
        self.tool_bar = QToolBar()
        self.tool_bar.addAction(self.new)
        self.tool_bar.addAction(self.open)
        self.tool_bar.addAction(self.save)
        self.tool_bar.addAction(self.cut)
        self.tool_bar.addAction(self.copy)
        self.tool_bar.addAction(self.paste)
        self.tool_bar.addAction(self.find)
        self.tool_bar.addAction(self.replace)

        #tool文本显示在下方
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)


        #表格
        self.table_view = QTableView()
        self.table_view.setModel(self.mode)

        #状态栏
        self.status_bar = QStatusBar()
        self.status_bar.showMessage('这是一个状态栏')


        #创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.menu)
        layout.addWidget(self.tool_bar)
        layout.addWidget(self.table_view)
        layout.addWidget(self.status_bar)
        self.setLayout(layout)

        #关联信号
        self.open.triggered.connect(self.clickOpen)

        #美化
        icon = QIcon()
        icon.addPixmap(QPixmap('./image/打开.png'), QIcon.Normal, QIcon.Off)
        self.open.setIcon(icon)

    def clickOpen(self):
        self.status_bar.showMessage('打开文件',5000)
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.AnyFile)
        dir = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Learn-python-notes'
        self.dialog.setDirectory(dir)
        self.dialog.setFilter(QDir.Files)
        if self.dialog.exec_():
            try:
                timer = QElapsedTimer()
                timer.start()
                file_name = self.dialog.selectedFiles()[0]
                data = read_xlsx(file_name)
                self.data = data
                print('init data need %s seconds' % (timer.elapsed() / 1000))
                # self.table_view.setModel(TableModel(data))
                self.mode = QStandardItemModel()
                for rows in data:
                    row = [QStandardItem(str(cell)) for cell in rows]
                    self.mode.appendRow(row)
                self.table_view.setModel(self.mode)
                print('input data need %s seconds' % (timer.elapsed() / 1000))
                self.status_bar.showMessage('数据加载完毕！！！')
            except Exception as e:
                print(e)
                pass




def read_xlsx(path):
    # timer = QElapsedTimer()
    # timer.start()
    workbook = xlrd.open_workbook(path)
    sheet1 = workbook.sheet_by_index(0)
    rows = len(sheet1.col_values(0))
    data = [sheet1.row_values(i) for i in range(rows)]
    # print(data)
    global  global_data
    global_data = data
    return data
    # print('init data need %s seconds' % (timer.elapsed() / 1000))
    # mode = TableModel(data)
    # print('input data need %s seconds' % (timer.elapsed() / 1000))
    # return mode



class InputWindowDemo(QTabWidget):
    def __init__(self):
        super(InputWindowDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500,100,1000,900)
        self.send = MyTypeSignal()

        #创建两个窗口
        #tab1：显示全部，tab2：只显示变量
        self.mode1 = QStandardItemModel(100,100)
        self.tab1 = WidgetDemo(self.mode1)
        self.mode2 = QStandardItemModel(100,100)
        self.tab2 = WidgetDemo(self.mode2)


        self.addTab(self.tab1,'数据视图')
        self.addTab(self.tab2,'变量视图')

        #tab放在底部
        self.setTabPosition(QTabWidget.TabPosition.South)
        #tab形状：设置为三角形：Triangular，圆角为：Rouned
        self.setTabShape(QTabWidget.Triangular)
        self.currentChanged.connect(self.getCurrentTab)

    def getCurrentTab(self,index):
        # print(index)
        '''
        数据从model中取出：
        可以用index（row，col）.data().to…,
        最后的to后面可以跟你想要的类型
        '''
        global global_data
        if index == 1 and global_data is not None:
            # print(global_data[0])
            #当已经导入数据时设置变量视图
            cnt = 0
            for cell in global_data[0]:
                if cell != '':
                    self.mode2.setItem(cnt,0,QStandardItem(str(cell)))
                    cnt += 1



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = InputWindowDemo()
    window.show()
    sys.exit(app.exec_())