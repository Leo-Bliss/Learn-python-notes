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
from PyQt5.QtWidgets import QTableView,QFileDialog
from PyQt5.QtWidgets import QMenuBar,QToolBar,QStatusBar
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QStandardItemModel,QPixmap,QIcon,QStandardItem
from PyQt5.QtCore import Qt,QDir,QElapsedTimer
from openpyxl import workbook
import xlrd


class WidgetDemo(QWidget):
    def __init__(self,mode):
        super(WidgetDemo,self).__init__()
        self.mode = mode
        self.initUI(mode)

    def initUI(self,mode):
        self.resize(800,800)
        #这里初始化，便于直接输入数据
        self.data = [['']*100 for i in range(100)]
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
        self.save.triggered.connect(self.clickSave)
        self.mode.itemChanged.connect(self.dealItemChanged)

        #美化
        icon = QIcon()
        icon.addPixmap(QPixmap('./image/打开.png'), QIcon.Normal, QIcon.Off)
        self.open.setIcon(icon)

    def clickOpen(self):
        self.status_bar.showMessage('打开文件',5000)
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.AnyFile)
        dir = r'D:/Learn-python-notes/projects/demo/Work/TCM_DSAS/data'
        self.dialog.setDirectory(dir)
        self.dialog.setFilter(QDir.Files)
        if self.dialog.exec_():
            try:
                timer = QElapsedTimer()
                timer.start()
                file_name = self.dialog.selectedFiles()[0]
                #这里读取数据返回列表便于表格中数据的更新
                data_list = read_xlsx(file_name)
                self.data = data_list
                print('init data need %s seconds' % (timer.elapsed() / 1000))
                self.mode = QStandardItemModel()
                for rows in data_list:
                    row = [QStandardItem(str(cell)) for cell in rows]
                    self.mode.appendRow(row)
                self.mode.itemChanged.connect(self.dealItemChanged)
                self.table_view.setModel(self.mode)

                print('input data need %s seconds' % (timer.elapsed() / 1000))
                self.status_bar.showMessage('数据加载完毕！！！')
            except Exception as e:
                print(e)
                pass

    def clickSave(self):
        file_path, self.save = QFileDialog.getSaveFileName(self, '保存文件', './data',
                                                           'ALL Files(*);;xlsx(*.xlsx);;xls(*.xls);;csv(*.csv);;txt(*.txt)')
        # print(file_path)
        wb = workbook.Workbook()
        wb.encoding='utf-8'
        wa = wb.active
        # 文件中写入数据
        try:
            for item in self.data:
                wa.append(item)
            wb.save(file_path)
        except Exception as e:
            pass

    #数据变化信号处理
    def dealItemChanged(self,item):
        print(u'位置(row:{},col:{})'.format(item.row(),item.column()) ,end='')
        print(u' 改变了值!')
        row,column = item.row(),item.column()
        self.data[row][column] = item.text()
        # print(self.data)
        print(u'新值为:', item.text())
        print('-'*100)


def read_xlsx(path):
    workbook = xlrd.open_workbook(path)
    sheet1 = workbook.sheet_by_index(0)
    rows = len(sheet1.col_values(0))
    data = [sheet1.row_values(i) for i in range(rows)]
    return data




class InputWindowDemo(QTabWidget):
    def __init__(self):
        super(InputWindowDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500,100,1000,900)

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
        #得到数据视图中的数据
        all_data = self.tab1.data

        # print(all_data[0])
        # 当已经导入数据时设置变量视图
        if index == 1 and all_data is not None:
            cnt = 0
            for cell in all_data[0]:
                if cell != '':
                    self.mode2.setItem(cnt,0,QStandardItem(str(cell)))
                    cnt += 1



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = InputWindowDemo()
    window.show()
    sys.exit(app.exec_())