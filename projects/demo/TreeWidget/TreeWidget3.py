#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    14:16  2019/11/25
#@Author  :    tb_youth
#@FileName:    TreeWidget3.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
QTreeView 控件与系统定制模式
QTreeWidget
Model
QDirModel
'''
import  sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeView,QDirModel


if __name__=='__main__':
    app = QApplication(sys.argv)
    model = QDirModel()
    tree = QTreeView()
    tree.setModel(model)
    tree.show()
    tree.resize(800,400)
    tree.setWindowTitle('QTreeView')
    sys.exit(app.exec_())
