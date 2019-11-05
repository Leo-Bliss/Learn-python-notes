#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/5 0005 22:41
#@Author  :    tb_youth
#@FileName:    QComBoxDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
1.如何添加列表项
2.如何获得列表项
'''

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QLabel,QComboBox,QHBoxLayout

class QComboxDemo(QWidget):
    def __init__(self):
        super(QComboxDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(500,200)
        self.setWindowTitle('QComboxDemo')

        self.label = QLabel('请选择编程语言')

        self.combox = QComboBox()
        # 为combox添加item
        self.combox.addItem('C')
        self.combox.addItem('C++')
        self.combox.addItem('Java')
        self.combox.addItems(['Python','C#','R'])
        #关联信号
        self.combox.currentIndexChanged.connect(self.selectionChange)
        #布局
        layout = QHBoxLayout()
        self.label.setMaximumSize(150,30)
        self.combox.setMaximumSize(100,30)
        layout.addWidget(self.label)
        layout.addWidget(self.combox)

        self.setLayout(layout)

    def selectionChange(self,i):
        #设置标签文本
        self.label.setText(self.combox.currentText())
        self.label.adjustSize()

        for index in range(self.combox.count()):
            #根据下标获取文本
            print('item' + str(index) + ' = ' + self.combox.itemText(index))
        #获取当前文本
        print('current index',i,'selection changed',self.combox.currentText())


if __name__=='__main__':
    app =QApplication(sys.argv)
    window = QComboxDemo()
    window.show()
    sys.exit(app.exec_())


