#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    10:15  2019/12/13
#@Author  :    tb_youth
#@FileName:    removeItem.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout
from PyQt5.QtWidgets import QListWidget,QPushButton,QGroupBox,QTreeWidget,QTreeWidgetItem
import sys



class MyApp(object):    
    def __init__(self):
        super(MyApp, self).__init__()                
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)

        self.hLayout = QHBoxLayout()
        self.mainLayout.insertLayout(0, self.hLayout)


        self.listA = QTreeWidget()
        self.listA.setColumnCount(3)
        self.listA.setHeaderLabels(['Checkbox','Name','Data'])

        for i in range(3):
            item = QTreeWidgetItem()
            item.setCheckState(0,QtCore.Qt.Checked)
            item.setText(1, 'Item '+str(i))
            item.setData(2, QtCore.Qt.UserRole, id(item) )
            item.setText(2, str(id(item) ) )
            self.listA.addTopLevelItem(item)

        self.hLayout.addWidget(self.listA)

        self.buttonGroupbox = QGroupBox()
        self.buttonlayout = QVBoxLayout()
        self.buttonGroupbox.setLayout(self.buttonlayout)

        okButton = QPushButton('Remove Selected')
        okButton.clicked.connect(self.removeSel)
        self.buttonlayout.addWidget(okButton)

        getDataButton = QPushButton('Get Items Data')
        getDataButton.clicked.connect(self.getItemsData)
        self.buttonlayout.addWidget(getDataButton)

        self.mainLayout.addWidget(self.buttonGroupbox)
        self.mainWidget.show()
        sys.exit(app.exec_())

    def removeSel(self):
        listItems=self.listA.selectedItems()
        if not listItems: return   
        for item in listItems:
            itemIndex=self.listA.indexOfTopLevelItem(item)
            self.listA.takeTopLevelItem(itemIndex)
        print('\n\t Number of items remaining', self.listA.topLevelItemCount())

    def getItemsData(self):
        for i in range(self.listA.topLevelItemCount()):
            item=self.listA.topLevelItem(i)
            itmData=item.data(2, QtCore.Qt.UserRole)
            itemId=itmData.toPyObject()
            print('\n\t Item Id Stored as Item Data:', itemId, 'Item Checkbox State:', item.checkState(0))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyApp()
