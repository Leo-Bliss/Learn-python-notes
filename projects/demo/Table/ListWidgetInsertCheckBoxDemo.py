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
from PyQt5.QtWidgets import QApplication,QWidget,QCheckBox,QListWidget,QVBoxLayout
from PyQt5.QtWidgets import QLineEdit,QPushButton,QHBoxLayout,QListWidgetItem,QFileDialog
import xlrd

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
        self.list_widget = QListWidget()
        '''
        self.check_box1 = QCheckBox('x1')
        self.check_box2 = QCheckBox('x2')
        self.check_box3 = QCheckBox()
        self.check_box3.setText('y1')

        item1 = QListWidgetItem()
        item2 = QListWidgetItem()
        item3 = QListWidgetItem()

        self.list_widget.addItem(item1)
        self.list_widget.addItem(item2)
        self.list_widget.addItem(item3)
        self.list_widget.setItemWidget(item1,self.check_box1)
        self.list_widget.setItemWidget(item2,self.check_box2)
        self.list_widget.setItemWidget(item3,self.check_box3)
        '''

        vlayout = QVBoxLayout()
        vlayout.addItem(hlayout1)
        vlayout.addItem(hlayout)
        vlayout.addWidget(self.list_widget)
        self.setLayout(vlayout)

        self.open_button.clicked.connect(self.open)
        self.button1.clicked.connect(self.selectAll)
        self.button2.clicked.connect(self.cancelSelectAll)

    def open(self):
        file_name,_=QFileDialog.getOpenFileName(self,'打开EXCEL','E:/','EXcel文件(*.xlsx *.xls *.csv)')
        print(file_name)
        #xlsx
        if file_name.find('.xlsx'):
            header_list = open_xlsx(file_name)
            self.cnt = len(header_list)
            for i in range(self.cnt):
                item = QListWidgetItem()
                check_box = QCheckBox(header_list[i])
                check_box.setChecked(True)
                self.list_widget.addItem(item)
                self.list_widget.setItemWidget(item,check_box)
                '''
                此处涉及到，到底是创建准确对象(有命名)还是临时对象的问题，
                创建准确对象，方便访问，但是有一个如何不断创建准确对象问题，
                创建临时对象，存在需要时该如何访问的问题
                '''
                #checkState(),True:2,False:0
                self.list_widget.item(i).listWidget().item(0).setCheckState()
                print(self.list_widget.item(i).listWidget().item(0).checkState())

        elif file_name.find('.xls'):
            pass
        else:
            pass


    def selectAll(self):
        self.cnt = self.list_widget.count()
        print(self.cnt)
        for i in range(1,self.cnt+1):
            item = 'self.check_box%s.setChecked(True)'%str(i)
            eval(item)

    def cancelSelectAll(self):
        self.cnt = self.list_widget.count()
        print(self.cnt)
        for i in range(1, self.cnt + 1):
            item = 'self.check_box%s.setChecked(False)' % str(i)
            eval(item)


def open_xlsx(file_name):
    wb = xlrd.open_workbook(file_name)
    sheet1 = wb.sheet_by_index(0)
    header_labels = sheet1.row_values(0)
    print(header_labels)
    return header_labels


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec_())




