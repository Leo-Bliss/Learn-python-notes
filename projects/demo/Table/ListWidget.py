#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    15:19  2019/10/22
#@Author  :    tb_youth
#@FileName:    ListWidget.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

from PyQt5.QtWidgets import QApplication,QMessageBox,QMainWindow,QListWidget,QWidget,QHBoxLayout

import sys

class ListWidgetDemo(QMainWindow):
    def __init__(self):
        super(ListWidgetDemo,self).__init__()
        self.resize(800,800)
        self.setWindowTitle('QListWidgetDemo')

        self.listwidget = QListWidget()
        self.listwidget.addItem('PLS')
        self.listwidget.addItem('KNN')
        self.listwidget.addItem('SVM')
        self.listwidget.addItem('Lasso')

        # layout = QHBoxLayout()
        # layout.addWidget(self.listwidget)
        # self.setLayout(layout)

        #如果继承QWidget，则没有此方法
        self.setCentralWidget(self.listwidget)

        self.listwidget.itemClicked.connect(self.clicked)

    def clicked(self,Index):
        QMessageBox.information(self,'QListWidget','您选择的是：'+self.listwidget.item(self.listwidget.row(Index)).text())


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = ListWidgetDemo()
    window.show()
    sys.exit(app.exec_())
