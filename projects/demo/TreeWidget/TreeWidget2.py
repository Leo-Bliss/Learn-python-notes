#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    11:19  2019/11/25
#@Author  :    tb_youth
#@FileName:    TreeWidget2.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
动态创建树的节点
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QTreeWidgetItem,QTreeWidget,QHBoxLayout,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon

class QTreeWidgetDemo2(QWidget):
    def __init__(self):
        super(QTreeWidgetDemo2,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('QTreeWidgetDemo2')

        self.button1 = QPushButton('add Node')
        self.button2 = QPushButton('delete Node')
        self.button3 = QPushButton('update Node')

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.button1)
        hlayout.addWidget(self.button2)
        hlayout.addWidget(self.button3)
        hlayout.setSpacing(20)

        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)

        self.tree.setHeaderLabels(['key', 'values'])

        root1 = QTreeWidgetItem(self.tree)
        root1.setText(0, '根节点')
        root1.setText(1, '根节点的数据')
        root1.setIcon(0, QIcon('./image/course.png'))
        self.tree.setColumnWidth(0, 160)

        child1 = QTreeWidgetItem(root1)
        child1.setText(0, '子节点1')
        child1.setText(1, '子节点1的数据')
        child1.setIcon(0, QIcon('./image/child.png'))

        child1 = QTreeWidgetItem(root1)
        child1.setText(0, '子节点2')
        child1.setText(1, '子节点2的数据')
        child1.setIcon(0, QIcon('./image/camera.png'))

        root2 = QTreeWidgetItem(self.tree)
        root2.setText(0, '根节点2')
        root2.setText(1, '根节点2的数据')
        root2.setIcon(0, QIcon('./image/address'))

        child2_1 = QTreeWidgetItem(root2)
        child2_1.setText(0, '子节点1')
        child2_1.setText(1, '子节点1的数据')
        child2_1.setIcon(0, QIcon('./image/bluetoothon.png'))

        vlayout = QVBoxLayout()
        vlayout.addItem(hlayout)
        vlayout.addWidget(self.tree)
        self.setLayout(vlayout)
        self.button1.clicked.connect(self.addNode)
        self.button2.clicked.connect(self.delNode)
        self.button3.clicked.connect(self.updateNode)

    def addNode(self):
        print('添加节点')
        item = self.tree.currentItem()
        print(item)
        node = QTreeWidgetItem(item)
        node.setText(0,'新节点')
        node.setText(1,'新节点的值')
        node.setIcon(0,QIcon('./image/child.png'))

    def delNode(self):
        print('删除节点')
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)

    def updateNode(self):
        print('修改节点')
        item = self.tree.currentItem()
        item.setText(0,'修改节点')
        item.setText(1,'值已修改')




if __name__=='__main__':
    app = QApplication(sys.argv)
    window = QTreeWidgetDemo2()
    window.show()
    sys.exit(app.exec_())