#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    14:47  2019/10/22
#@Author  :    tb_youth
#@FileName:    ListView.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth



from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QMessageBox
from PyQt5.QtCore import QStringListModel
import sys

class ListViewDemo(QWidget):
    def __init__(self):
        super(ListViewDemo,self).__init__()
        self.resize(800,800)
        self.setWindowTitle('ListViewDemo')

        listview = QListView()
        listModel = QStringListModel()
        self.list = ['PLS','SVM','KNN','Lasso']
        listModel.setStringList(self.list)

        # 关联model

        listview.setModel(listModel)
        #绑定事件
        listview.clicked.connect(self.clicked)
        #设置控件布局
        layout = QVBoxLayout()
        layout.addWidget(listview)
        self.setLayout(layout)

    def clicked(self,item):
        QMessageBox.information(self,"QlistView","您选择了："+self.list[item.row()])


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = ListViewDemo()
    window.show()
    sys.exit(app.exec_())

