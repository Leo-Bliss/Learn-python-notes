#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    9:28  2019/12/10
#@Author  :    tb_youth
#@FileName:    temp.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random


class Splash(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(500,500)
        # CREATE THE TABLE
        self.table = QTableView(self)  # SELECTING THE VIEW
        self.table.setGeometry(0, 0, 575, 575)
        self.model = QStandardItemModel(self)  # SELECTING THE MODEL - FRAMEWORK THAT HANDLES QUERIES AND EDITS
        self.table.setModel(self.model)  # SETTING THE MODEL
        # self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.populate()
        self.btn1 = QPushButton('获取数据')
        self.btn2 = QPushButton('增加一行')
        self.btn3 = QPushButton('删除一行')
        self.btn4 = QPushButton('增加一列')
        self.btn5 = QPushButton('删除一列')
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        layout.addWidget(self.btn5)
        self.setLayout(layout)


        self.table.clicked.connect(self.on_click)
        self.btn1.clicked.connect(self.get_data)
        self.btn2.clicked.connect(self.addRow)
        self.btn3.clicked.connect(lambda: self.model.removeRow(self.table.currentIndex().row()))
        self.btn4.clicked.connect(self.addColumn)
        self.btn5.clicked.connect(lambda: self.model.removeColumn(self.table.currentIndex().column()))


    def on_click(self, signal):
        row = signal.row()  # RETRIEVES ROW OF CELL THAT WAS DOUBLE CLICKED
        column = signal.column()  # RETRIEVES COLUMN OF CELL THAT WAS DOUBLE CLICKED
        cell_dict = self.model.itemData(signal)  # RETURNS DICT VALUE OF SIGNAL
        cell_value = cell_dict.get(0)  # RETRIEVE VALUE FROM DICT

        index = signal.sibling(row, 0)
        index_dict = self.model.itemData(index)
        index_value = index_dict.get(0)
        print('Row {}, Column {} clicked - value: {}\nColumn 1 contents: {}'.format(row, column, cell_value, index_value))

    def get_data(self):
        rows = self.model.rowCount()
        columns = self.model.columnCount()

        for i in range(rows):
            for j in range(columns):
                print(self.model.index(i,j).data(),end = ' ')
            print()

    def addRow(self):
        self.model.insertRows(self.model.rowCount(),1)

    def addColumn(self):
        self.model.insertColumns(self.model.columnCount(), 1)




    def populate(self):
        # GENERATE A 4x10 GRID OF RANDOM NUMBERS.
        # VALUES WILL CONTAIN A LIST OF INT.
        # MODEL ONLY ACCEPTS STRINGS - MUST CONVERT.
        values = []
        for i in range(10):
            sub_values = []
            for i in range(4):
                value = random.randrange(1, 100)
                sub_values.append(value)
            values.append(sub_values)

        for value in values:
            row = []
            for item in value:
                cell = QStandardItem(str(item))
                row.append(cell)
            self.model.appendRow(row)

        # self.show()


if __name__ == '__main__':
    # import sys
    # app = QApplication(sys.argv)
    # ex = Splash()
    # ex.show()
    # sys.exit(app.exec_())
    data = [[1,2,3] for i in range(3)]
    print(data)
    data[1][1] = 5
    print(data)
    print(data[1][1])
    import numpy as np
    num = np.array(data)
    print(num)
    print(num[1,1])
    num[2,1] = 6
    print(num)
