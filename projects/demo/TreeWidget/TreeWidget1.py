#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    10:36  2019/11/25
#@Author  :    tb_youth
#@FileName:    TreeWidget1.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
创建QTreeWidget
并添加单击事件
'''

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeWidget,QTreeWidgetItem
from PyQt5.QtGui import QIcon

class QTreeWidgetDemo(QMainWindow):
    def __init__(self):
        super(QTreeWidgetDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('TreeWidget')
        self.setWindowIcon(QIcon('./image/favoriteslist.png'))

        self.tree = QTreeWidget()
        self.setCentralWidget(self.tree)
        self.tree.setColumnCount(2)

        self.tree.setHeaderLabels(['key','values'])

        root1 = QTreeWidgetItem(self.tree)
        root1.setText(0,'根节点')
        root1.setText(1,'根节点的数据')
        root1.setIcon(0,QIcon('./image/course.png'))
        self.tree.setColumnWidth(0,160)

        child1 = QTreeWidgetItem(root1)
        child1.setText(0,'子节点1')
        child1.setText(1,'子节点1的数据')
        child1.setIcon(0,QIcon('./image/child.png'))

        child1 = QTreeWidgetItem(root1)
        child1.setText(0, '子节点2')
        child1.setText(1, '子节点2的数据')
        child1.setIcon(0, QIcon('./image/camera.png'))

        root2 = QTreeWidgetItem(self.tree)
        root2.setText(0,'根节点2')
        root2.setText(1,'根节点2的数据')
        root2.setIcon(0,QIcon('./image/address'))

        child2_1 = QTreeWidgetItem(root2)
        child2_1.setText(0, '子节点1')
        child2_1.setText(1, '子节点1的数据')
        child2_1.setIcon(0, QIcon('./image/bluetoothon.png'))

        #展开所有节点
        self.tree.expandAll()
        self.tree.clicked.connect(self.onClickedTree)

    def onClickedTree(self,index):
        item = self.tree.currentItem()
        print(index.row())
        print('key = %s values = %s'%(item.text(0),item.text(1)))



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = QTreeWidgetDemo()
    window.show()
    sys.exit(app.exec_())




