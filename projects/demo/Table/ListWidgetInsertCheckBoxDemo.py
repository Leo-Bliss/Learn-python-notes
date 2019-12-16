#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/12 0012 21:55
#@Author  :    tb_youth
#@FileName:    ListWidgetInsertCheckBoxDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth
'''
实现的功能：
1.在listWidget中加入checkBox
2.全选，全不选功能，
3.打开excel，将表格水平标签设置为check_box的文本内容
'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QCheckBox,QListWidget,QVBoxLayout,QAbstractItemView
from PyQt5.QtWidgets import QLineEdit,QPushButton,QHBoxLayout,QListWidgetItem,QFileDialog

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.cnt = 0
        self.initUI()
    def initUI(self):
        self.resize(600,600)
        self.setWindowTitle('checkBox放入QListWidget')

        self.line_edit1 = QLineEdit()
        self.line_edit1.setPlaceholderText('文件路径')
        self.open_button = QPushButton('打开')
        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self.line_edit1)
        hlayout1.addWidget(self.open_button)

        self.button1 = QPushButton('确认全选')
        self.button2 = QPushButton('取消全选')
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.button1)
        hlayout.addWidget(self.button2)
        self.list_widget1 = QListWidget()
        '''
        self.check_box1 = QCheckBox('x1')
        self.check_box2 = QCheckBox('x2')
        self.check_box3 = QCheckBox()
        self.check_box3.setText('y1')

        item1 = QListWidgetItem()
        item2 = QListWidgetItem()
        item3 = QListWidgetItem()

        self.list_widget1.addItem(item1)
        self.list_widget1.addItem(item2)
        self.list_widget1.addItem(item3)
        self.list_widget1.setItemWidget(item1,self.check_box1)
        self.list_widget1.setItemWidget(item2,self.check_box2)
        self.list_widget1.setItemWidget(item3,self.check_box3)
        '''
        self.list_widget2 = QListWidget()
        self.list_widget1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.button3 = QPushButton('<=>')
        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(self.list_widget1)
        hlayout2.addWidget(self.button3)
        hlayout2.addWidget(self.list_widget2)
        vlayout = QVBoxLayout()
        vlayout.addItem(hlayout1)
        vlayout.addItem(hlayout)
        vlayout.addItem(hlayout2)
        self.setLayout(vlayout)

        self.open_button.clicked.connect(self.open)
        self.button1.clicked.connect(self.selectAllStatus)
        self.button2.clicked.connect(self.selectAllStatus)
        self.button3.clicked.connect(self.add)


    def open(self):
        file_dir = 'E:/' if self.line_edit1.text()=='' else self.line_edit1.text()
        file_name,_=QFileDialog.getOpenFileName(self,'打开EXCEL',file_dir,'Excel文件(*.xlsx *.xls *.csv)')
        print(file_name)
        if file_name == '':
            return
        self.line_edit1.setText(file_name)
        header_list = read_xlsx(file_name)[0]
        self.cnt = len(header_list)
        for i in range(self.cnt):
            item = QListWidgetItem()
            # print('&&&', item)
            check_box = QCheckBox(header_list[i])
            check_box.setChecked(True)
            # print('@@@', check_box)
            self.list_widget1.addItem(item)
            self.list_widget1.setItemWidget(item, check_box)
            '''
            此处涉及到，到底是创建准确对象(有命名)还是临时对象的问题，
            创建准确对象，方便访问，但是有一个如何不断创建准确对象问题，
            创建临时对象，存在需要时该如何访问的问题。
            前者暂时没有解决，我采用后者
            '''
            # 访问之前创建的临时对象
            now_item = self.list_widget1.item(i).listWidget().item(i)
            # print(now_item)
            now_check_box = self.list_widget1.item(i).listWidget().itemWidget(now_item)
            now_check_box.clicked.connect(self.getCheckBoxStatus)


    def getCheckBoxStatus(self):
        for i in range(self.list_widget1.count()):
            now_item = self.list_widget1.item(i).listWidget().item(i)
            now_check_box = self.list_widget1.item(i).listWidget().itemWidget(now_item)

    def selectAllStatus(self):
        sender = self.sender()
        print(sender.text())
        status = sender.text() == '确认全选'
        for i in range(self.list_widget1.count()):
            now_item = self.list_widget1.item(i).listWidget().item(i)
            now_check_box = self.list_widget1.item(i).listWidget().itemWidget(now_item)
            now_check_box.setChecked(status)

    def innnerSelectAll(self):
        #全选
        self.list_widget1.selectAll()

        # #取消全选
        # self.list_widget1.clearSelection()

        # # 将选中项移除
        # for selectedItem in self.list_widget1.selectedItems():
        #     self.list_widget1.takeItem(self.list_widget1.row(selectedItem))

    def add(self):
        count = self.list_widget1.count()
        index = 0
        while index < count:
            now_item = self.list_widget1.item(index).listWidget().item(index)
            now_check_box = self.list_widget1.item(index).listWidget().itemWidget(now_item)
            if(now_check_box.isChecked()):
                item = QListWidgetItem()
                check_box = QCheckBox(now_check_box.text())
                check_box.setChecked(True)
                self.list_widget2.addItem(item)
                self.list_widget2.setItemWidget(item, check_box)
                self.list_widget1.takeItem(index)
                count -= 1
            else:
                index += 1



#xls,xlxs,csv
def read_xlsx(path):
    import xlrd
    workbook = xlrd.open_workbook(path)
    sheet1 = workbook.sheet_by_index(0)
    rows = len(sheet1.col_values(0))
    data = [sheet1.row_values(i) for i in range(rows)]
    return data



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec_())




