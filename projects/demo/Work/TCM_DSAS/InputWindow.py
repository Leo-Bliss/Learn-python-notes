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
from PyQt5.QtWidgets import QApplication,QWidget,QTabWidget,QMenu,qApp
from PyQt5.QtWidgets import QTableView,QFileDialog,QPushButton
from PyQt5.QtWidgets import QMenuBar,QToolBar,QStatusBar,QAction,QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout,QSizePolicy,QLineEdit
from PyQt5.QtGui import QStandardItemModel,QPixmap,QIcon,QStandardItem,QColor,QCursor
from PyQt5.QtCore import Qt,QDir,QThread,pyqtSignal,QObject
from openpyxl import workbook
# from PyQt5.QtSql import QSqlDatabase,QSqlTableModel
import DataFrameListMTF
import xlrd
import csv


import VariableSettingWindow
#自定义的信号类，用于窗口通信

class MySignal(QObject):
    sender = pyqtSignal(QStandardItemModel)
    def send(self,model):
        self.sender.emit(model)

#查找替换窗口
class  FindWidget(QWidget):
    def __init__(self):
        super(FindWidget,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(80,800)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)

        self.line_edit1 = QLineEdit()
        self.line_edit1.setPlaceholderText('find')
        self.line_edit2 = QLineEdit()
        self.line_edit2.setPlaceholderText('replace')

        self.tool_bar = QToolBar()
        self.search = QAction('查找')
        self.up_aciton = QAction('向上')
        self.down_aciton = QAction('向下')
        self.close_aciton= QAction('关闭')
        self.tool_bar.addAction(self.search)
        self.tool_bar.addAction(self.down_aciton)
        self.tool_bar.addAction(self.up_aciton)
        self.tool_bar.addAction(self.close_aciton)

        self.repalce_button = QPushButton('Replace')
        self.repalceAll_button = QPushButton('ReplaceAll')

        vlayout1 = QVBoxLayout()
        vlayout1.addWidget(self.line_edit1)
        vlayout1.addWidget(self.line_edit2)

        vlayout2 = QVBoxLayout()
        vlayout2.addWidget(self.tool_bar)

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self.repalce_button)
        hlayout1.addWidget(self.repalceAll_button)
        vlayout2.addItem(hlayout1)

        layout = QHBoxLayout()
        layout.addItem(vlayout1)
        layout.addItem(vlayout2)
        self.setLayout(layout)

        self.close_aciton.triggered.connect(self.triggeredClose)
        icon = QIcon()
        icon.addPixmap(QPixmap('./image/查找.png'), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon)
        icon.addPixmap(QPixmap('./image/向下.png'), QIcon.Normal, QIcon.Off)
        self.down_aciton.setIcon(icon)
        icon.addPixmap(QPixmap('./image/向上.png'), QIcon.Normal, QIcon.Off)
        self.up_aciton.setIcon(icon)
        icon.addPixmap(QPixmap('./image/关闭.png'), QIcon.Normal, QIcon.Off)
        self.close_aciton.setIcon(icon)

    def triggeredClose(self):
        self.hide()




class ReaderExcelThread(QThread):
    standarModel_signal = pyqtSignal(QStandardItemModel)
    # sqlTableModel_signal = pyqtSignal(QSqlTableModel)
    progressRate_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()
    # '''
    # 读取表格的方式分为两种：
    # 1.读取后直接使用，即直接设置并返回为QStandardItemModel
    # 2.读取后放到缓存数据库，从数据库中取数据，返回QSqlTableModel
    # '''
    def __init__(self,file_name,operate_way=1):
        super().__init__()
        self.file_name = file_name
        self.operate_way = operate_way
        self.model = QStandardItemModel()

    def run(self):
        # 这里读取数据返回列表便于表格中数据的更新
        self.progressRate_signal.emit("数据载入准备中...")
        data_list = read_excel(self.file_name)
        if data_list == -1:
            return
        print('start work!')
        cnt = len(data_list)
        for i,rows in enumerate(data_list):
            row = [QStandardItem(str(cell)) for cell in rows]
            self.model.appendRow(row)
            percent = int(i / cnt * 100 + 0.5)
            self.progressRate_signal.emit("数据载入进度:{}%".format(percent))

        #自动填满，这样更加美观（不过增加了后期数据处理难度！）
        while self.model.rowCount() < 22:
            self.model.insertRows(self.model.rowCount(),1)
        while self.model.columnCount() < 15:
            self.model.insertColumns(self.model.columnCount(),1)

        #数据加载完成
        self.progressRate_signal.emit("数据载入进度:100%")
        self.standarModel_signal.emit(self.model)
        print('send finised')
        self.finished_signal.emit()


class WriteExcelThread(QThread):
    start_signal = pyqtSignal(str)
    end_signal = pyqtSignal()
    def __init__(self,file_path,model):
        super(QThread,self).__init__()
        self.file_path = file_path
        self.model = model

    def run(self):
        self.start_signal.emit('导出准备中...')
        try:
            dtl = DataFrameListMTF.DataFrameListMTF()
            data_list = dtl.model_to_list(self.model)
            wb = workbook.Workbook()
            wb.encoding = 'utf-8'
            wa = wb.active
            cnt = len(data_list)
            for i,item in enumerate(data_list):
                wa.append(item)
                self.start_signal.emit('导出进度:{}%'.format(int(i/cnt*100)))
            wb.save(self.file_path)
            self.start_signal.emit('导出进度:100%')
            self.end_signal.emit()
        except Exception as e:
            print(e)

# class GetVarThread(QThread):
#     send_signal = pyqtSignal(list)
#     end_signal = pyqtSignal()
#     def __init__(self,model):
#         super().__init__()
#         self.model = model
#
#     def run(self):
#         rows = self.model.rowCount()
#         columns = self.model.columnCount()
#         row_values = []
#         for row in range(rows):
#             row_values = [self.model.index(row, column).data() for column in range(columns)]
#             break
#         var_list = [value for value in row_values if value != '']
#         self.send_signal.emit(var_list)
#         self.end_signal.emit()

class WidgetDemo(QWidget):
    def __init__(self,model,rows,columns):
        super(WidgetDemo,self).__init__()
        self.init_rows = rows
        self.init_columns = columns
        self.model = model
        self.initUI(model)

    def initUI(self,model):
        self.resize(800,800)
        self.res_pos = []
        self.focus_pos = None
        self.var_list = None
        self.signal = MySignal()
        #菜单栏
        self.menu = QMenuBar()
        self.file = self.menu.addMenu('文件')
        self.edit = self.menu.addMenu('编辑')
        self.view = self.menu.addMenu('视图')
        self.help = self.menu.addMenu('帮助')
        #各菜单下的子菜单

        #文件菜单下的子菜单
        # self.new = self.file.addAction('新建')
        self.open = self.file.addAction('打开')
        self.save = self.file.addAction('保存')
        # self.save_as = self.file.addAction('另存为')


        #编辑菜单下的子菜单
        self.cut = self.edit.addAction('剪切')
        self.copy = self.edit.addAction('复制')
        self.paste = self.edit.addAction('粘贴')
        self.delete = self.edit.addAction('删除')
        self.find = self.edit.addAction('查找')
        self.replace = self.edit.addAction('替换')

        # 快捷键
        self.open.setShortcut('Ctrl+O')
        self.save.setShortcut('Ctrl+S')
        # self.new.setShortcut('Ctrl+N')
        self.find.setShortcut('Ctrl+F')

        #视图菜单下的子菜单
        self.tool_view = QAction('工具栏',checkable=True)
        self.tool_view.setChecked(True)
        self.view.addAction(self.tool_view)

        self.statu_view = QAction('状态栏',checkable=True)
        self.statu_view.setChecked(True)
        self.view.addAction(self.statu_view)


        #帮助菜单下的子菜单
        self.about = self.help.addAction('关于')

        #工具栏
        self.tool_bar = QToolBar()
        # self.tool_bar.addAction(self.new)
        self.tool_bar.addAction(self.open)
        self.tool_bar.addAction(self.save)
        self.tool_bar.addAction(self.cut)
        self.tool_bar.addAction(self.copy)
        self.tool_bar.addAction(self.paste)
        self.tool_bar.addAction(self.find)
        # self.setting = QAction('变量设置')
        # self.setting.setEnabled(False)
        # self.tool_bar.addAction(self.setting)
        # self.tool_bar.addAction(self.replace)

        # #tool文本显示在下方
        # self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        #findWidge
        self.find_widget = FindWidget()
        self.find_widget.hide()

        #表格
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        #状态栏
        self.status_bar = QStatusBar()
        self.status_bar.showMessage('状态栏')

        # 右键菜单栏
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.context_menu = QMenu()
        self.addRow_action = self.context_menu.addAction('增加一行')
        self.addRow_action.triggered.connect(self.addRow)
        self.delRow_action = self.context_menu.addAction('删除一行')
        self.delRow_action.triggered.connect(lambda: self.model.removeRow(self.table_view.currentIndex().row()))
        self.addColumn_action = self.context_menu.addAction('增加一列')
        self.addColumn_action.triggered.connect(self.addColumn)
        self.delColumn_action = self.context_menu.addAction('删除一列')
        self.delColumn_action.triggered.connect(lambda: self.model.removeColumn(self.table_view.currentIndex().column()))
        self.customContextMenuRequested.connect(self.rightMenuShow)

        #创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.menu)
        layout.addWidget(self.tool_bar)
        layout.addWidget(self.find_widget)
        layout.addWidget(self.table_view)
        layout.addWidget(self.status_bar)
        self.setLayout(layout)

        #关联信号
        self.open.triggered.connect(self.triggeredOpen)
        self.save.triggered.connect(self.triggeredSave)
        self.tool_view.triggered.connect(self.triggeredView)
        self.statu_view.triggered.connect(self.triggeredView)
        # self.new.triggered.connect(self.triggeredNew)
        self.find.triggered.connect(self.triggeredFind)
        self.find_widget.search.triggered.connect(self.dataLocation)
        self.find_widget.down_aciton.triggered.connect(self.downAcitonLocation)
        self.find_widget.up_aciton.triggered.connect(self.upAcitonLocation)
        self.find_widget.close_aciton.triggered.connect(self.triggeredHideFind)
        self.find_widget.repalce_button.clicked.connect(self.onClickReplace)
        self.find_widget.repalceAll_button.clicked.connect(self.onClickReplaceAll)
        # self.setting.triggered.connect(self.triggeredSetting)


        #美化
        icon = QIcon()
        icon.addPixmap(QPixmap('./image/打开.png'), QIcon.Normal, QIcon.Off)
        self.open.setIcon(icon)
        icon.addPixmap(QPixmap('./image/保存.png'), QIcon.Normal, QIcon.Off)
        self.save.setIcon(icon)
        # icon.addPixmap(QPixmap('./image/新建.png'), QIcon.Normal, QIcon.Off)
        # self.new.setIcon(icon)
        icon.addPixmap(QPixmap('./image/剪切.png'), QIcon.Normal, QIcon.Off)
        self.cut.setIcon(icon)
        icon.addPixmap(QPixmap('./image/复制.png'), QIcon.Normal, QIcon.Off)
        self.copy.setIcon(icon)
        icon.addPixmap(QPixmap('./image/粘贴.png'), QIcon.Normal, QIcon.Off)
        self.paste.setIcon(icon)
        icon.addPixmap(QPixmap('./image/查找1.png'), QIcon.Normal, QIcon.Off)
        self.find.setIcon(icon)
        # icon.addPixmap(QPixmap('./image/设置.png'), QIcon.Normal, QIcon.Off)
        # self.setting.setIcon(icon)
        # icon.addPixmap(QPixmap('./image/替换.png'), QIcon.Normal, QIcon.Off)
        # self.replace.setIcon(icon)

    def showProgress(self,msg):
        self.status_bar.showMessage(msg)

    def loadData(self,model):
        print('load...')
        self.model = model
        self.table_view.setModel(self.model)
        qApp.processEvents()


    def triggeredOpen(self):
        self.status_bar.showMessage('打开文件',5000)
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.AnyFile)
        dir = r'D:/Learn-python-notes/projects/demo/Work/TCM_DSAS/data'
        self.dialog.setDirectory(dir)
        self.dialog.setFilter(QDir.Files)
        if self.dialog.exec_():
            try:
                file_name = self.dialog.selectedFiles()[0]
                #这里线程实例化一定要实例化成员变量，否则线程容易销毁
                self.thread = ReaderExcelThread(file_name)
                self.thread.standarModel_signal.connect(self.loadData)
                self.thread.progressRate_signal.connect(self.showProgress)
                self.thread.finished_signal.connect(self.thread.quit)
                self.thread.start()
                # self.setting.setEnabled(True)
            except Exception as e:
                print(e)
                pass

    def triggeredSave(self):
        self.status_bar.showMessage('保存文件', 5000)
        file_path, _ = QFileDialog.getSaveFileName(self, '保存文件', './data',
                                                           'ALL Files(*);;xlsx(*.xlsx);;xls(*.xls);;csv(*.csv)')
        if file_path == '':
            return
        # 文件中写入数据
        try:
            self.write_thread = WriteExcelThread(file_path,self.model)
            self.write_thread.start_signal.connect(self.showProgress)
            self.write_thread.end_signal.connect(self.write_thread.quit)
            self.write_thread.start()
            self.status_bar.showMessage('保存完毕！')
        except Exception as e:
            print(e)



    #状态栏与工具栏的显示和隐藏
    def triggeredView(self,state):
        sender = self.sender().text()
        if sender == '工具栏':
            if state:
                self.tool_bar.show()
            else:
                self.tool_bar.hide()
        else:
            if state:
                self.status_bar.show()
            else:
                self.status_bar.hide()

    # def triggeredNew(self):
    #     print('New')
    #     pass

    def triggeredFind(self):
        self.find_widget.show()

    #重载信号，实现ESC隐藏查找窗口
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.find_widget.hide()

    #聚焦到某个cell
    def positionFocus(self,x,y):
        self.table_view.verticalScrollBar().setSliderPosition(x)
        self.table_view.horizontalScrollBar().setSliderPosition(y)
        self.table_view.openPersistentEditor(self.model.index(x, y))
        self.table_view.setFocus()

    #得到所以匹配项的位置
    def dataLocation(self):
        self.changeCellColor()
        text = self.find_widget.line_edit1.text()
        self.res_pos = []
        flag = 0
        rows = self.model.rowCount()
        columns = self.model.columnCount()
        try:
            for row in range(rows):
                for column in range(columns):
                    if text == self.model.index(row,column).data():
                        self.res_pos.append((row,column))
                        item = self.model.item(row,column)
                        item.setBackground(QColor(255, 255, 0))
                        item.setForeground(QColor(255, 0, 0))
                        #转到到第一个匹配值的位置，并处于可编辑状态
                        if not flag:
                            flag = 1
                            self.positionFocus(row,column)
                            self.focus_pos = 0
        except Exception as e:
            print(e)

    #向下跳转
    def downAcitonLocation(self):
        cnt = len(self.res_pos)
        if cnt == 0 or self.focus_pos == cnt-1:
            return
        try:
            self.table_view.closePersistentEditor(
                self.model.index(self.res_pos[self.focus_pos][0],self.res_pos[self.focus_pos][1]))
            x, y = self.res_pos[self.focus_pos + 1]
            self.positionFocus(x,y)
            self.focus_pos += 1
        except Exception as e:
            print(e)

    # 向上跳转
    def upAcitonLocation(self):
        cnt = len(self.res_pos)
        if cnt == 0 or self.focus_pos == 0:
            return
        try:
            self.table_view.closePersistentEditor(
                self.model.index(self.res_pos[self.focus_pos][0], self.res_pos[self.focus_pos][1]))
            x, y = self.res_pos[self.focus_pos - 1]
            self.positionFocus(x, y)
            self.focus_pos -= 1
        except Exception as e:
            print(e)


    def triggeredHideFind(self):
        self.changeCellColor()
        self.find_widget.hide()

    def changeCellColor(self):
        if self.res_pos is not None and len(self.res_pos):
            self.table_view.closePersistentEditor(
                self.model.index(self.res_pos[self.focus_pos][0], self.res_pos[self.focus_pos][1]))
            for item in self.res_pos:
                x, y = item
                item = self.model.item(x, y)
                item.setBackground(QColor(255, 255, 255))
                item.setForeground(QColor(0, 0, 0))


    def onClickReplace(self):
        cnt = len(self.res_pos)
        text = self.find_widget.line_edit2.text()
        if self.res_pos is None or cnt == 0:
            return
        try:
            x, y = self.res_pos[self.focus_pos]
            self.model.setItem(x,y,QStandardItem(text))
        except Exception as e:
            print(e)

    def onClickReplaceAll(self):
        cnt = len(self.res_pos)
        if self.res_pos is None or cnt == 0:
            return
        try:
            text = self.find_widget.line_edit2.text()
            for x,y in self.res_pos:
                self.model.setItem(x, y, QStandardItem(text))
        except Exception as e:
            print(e)

    # #设置变量
    # def triggeredSetting(self):
    #     self.getVar_thread = GetVarThread(self.model)
    #     self.getVar_thread.send_signal.connect(self.initVarList)
    #     self.getVar_thread.end_signal.connect(self.getVar_thread.quit)
    #     self.getVar_thread.start()
    #
    #
    #
    # def initVarList(self,var_list):
    #     dialog = VariableSettingWindow.VariableSettingWindowDemo(var_list)
    #     dialog.signal.sender.connect(self.getVarList)
    #     dialog.show()
    #
    # def getVarList(self,lst):
    #     self.var_list = lst
        # print(lst)

    def addRow(self):
        # 当前行的下方添加一行
        try:
            self.model.insertRows(self.table_view.currentIndex().row() + 1, 1)
        except Exception as e:
            print(e)

    def addColumn(self):
        self.model.insertColumns(self.table_view.currentIndex().column() + 1, 1)

    def rightMenuShow(self):
        try:
            #菜单显示的位置
            self.context_menu.popup(QCursor.pos())
            self.context_menu.show()
        except Exception as e:
            print(e)


# def modelToList(model):
#     # model = QStandardItemModel()
#     rows = model.rowCount()
#     columns = model.columnCount()
#     data_list = []
#     for row in range(rows):
#         row_values = [model.index(row,column).data() for column in range(columns)]
#         # print(row_values)
#         data_list.append(row_values)
#     # dtl = DataFrameListMTF.DataFrameListMTF()
#     # df = dtl.list_to_DataFrame(data_list)
#     return data_list


# xls,xlsx,csv

def read_excel(path):
    name, type = path.rsplit('.', maxsplit=1)
    if type == 'csv':
        with open(path, newline='') as f:
            reader = csv.reader(f, delimiter=',')
            data = [line for line in reader]
            return data
    elif type in ['xlsx', 'xls']:
        workbook = xlrd.open_workbook(path)
        sheet1 = workbook.sheet_by_index(0)
        rows = len(sheet1.col_values(0))
        data = [sheet1.row_values(i) for i in range(rows)]
        return data
    else:
        print('{}文件格式不支持'.format(type))
        return -1

def write_excel(file_path,data_list):
    try:
        wb = workbook.Workbook()
        wb.encoding = 'utf-8'
        wa = wb.active
        for item in data_list:
            wa.append(item)
        wb.save(file_path)
    except Exception as e:
        print(e)



class InputWindowDemo(QTabWidget):
    def __init__(self):
        super(InputWindowDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500,100,1000,900)
        self.setWindowIcon(QIcon('./image/导入.png'))

       #表格初始大小设置为22行,15列
        rows,columns = 22,15
        self.model = QStandardItemModel(rows,columns )
        self.data_view_tab = WidgetDemo(self.model,rows,columns )

        self.addTab(self.data_view_tab,'数据视图')

        #tab放在底部
        self.setTabPosition(QTabWidget.TabPosition.South)
        #tab形状：设置为三角形：Triangular，圆角为：Rouned
        self.setTabShape(QTabWidget.Triangular)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = InputWindowDemo()
    window.show()
    sys.exit(app.exec_())