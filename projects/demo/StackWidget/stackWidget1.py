#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    15:26  2019/11/25
#@Author  :    tb_youth
#@FileName:    stackWidget1.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth


import sys
from PyQt5.QtWidgets import *

class StackWidgetDemo(QWidget):
    def __init__(self):
        super(StackWidgetDemo,self).__init__()
        self.initUI()

    def initUI(self):
        # setGeometry参数：左上角坐标，宽高
        self.setGeometry(800,300,400,400)
        self.setWindowTitle('QStackedWidgetDemo')

        self.list = QListWidget()
        self.list.insertItem(0,'base information')
        self.list.insertItem(1, 'personal information')
        self.list.insertItem(2, 'course information')
        #设置item间隔
        self.list.setSpacing(5)

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.initStack1UI()
        self.initStack2UI()
        self.initStack3UI()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.list)
        hlayout.addWidget(self.stack)
        self.setLayout(hlayout)
        self.list.currentRowChanged.connect(self.disPlayStack)



    def initStack1UI(self):
        form_layout = QFormLayout()
        line_eidt1 = QLineEdit()
        line_eidt2 = QLineEdit()
        form_layout.addRow(QLabel('name:'), line_eidt1)
        form_layout.addRow(QLabel('id:'), line_eidt2)
        self.stack1.setLayout(form_layout)


    def initStack2UI(self):
        form_layout = QFormLayout()
        sex = QHBoxLayout()
        # comb = QComboBox()
        # comb.addItems(['18','19','20'])
        # form_layout.addRow(QLabel('age:'),comb)
        spinb = QSpinBox()
        spinb.setValue(18)
        spinb.setRange(18, 100)
        form_layout.addRow(QLabel('age:'), spinb)
        sex.addWidget(QRadioButton('male'))
        sex.addWidget(QRadioButton('female'))
        form_layout.addRow(QLabel('sex:'), sex)
        form_layout.addRow(QLabel('email:'), QLineEdit())
        form_layout.addRow(QLabel('address:'), QLineEdit())
        self.stack2.setLayout(form_layout)


    def initStack3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('course'))
        layout.addWidget(QCheckBox('math'))
        layout.addWidget(QCheckBox('english'))
        self.stack3.setLayout(layout)

    def disPlayStack(self,index):
        self.stack.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StackWidgetDemo()
    window.show()
    sys.exit(app.exec_())