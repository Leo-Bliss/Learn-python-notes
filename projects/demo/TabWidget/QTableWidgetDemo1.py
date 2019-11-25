#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    14:30  2019/11/25
#@Author  :    tb_youth
#@FileName:    QTableWidgetDemo1.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import *

class QTabWidgetDemo1(QTabWidget):
    def __init__(self):
        super(QTabWidgetDemo1,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(400,400)
        self.setWindowTitle('TabWidgetDemo')

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1,'选项卡1')
        self.addTab(self.tab2,'选项卡2')
        self.addTab(self.tab3,'选项卡3')
        self.initTab1UI()
        self.initTab2UI()
        self.initTab3UI()

    def initTab1UI(self):
        form_layout = QFormLayout()
        line_eidt1 = QLineEdit()
        line_eidt2 = QLineEdit()
        form_layout.addRow(QLabel('name:'),line_eidt1)
        form_layout.addRow(QLabel('id:'),line_eidt2)
        self.setTabText(0,'base information')
        self.tab1.setLayout(form_layout)

    def initTab2UI(self):
        form_layout = QFormLayout()
        sex = QHBoxLayout()
        # comb = QComboBox()
        # comb.addItems(['18','19','20'])
        # form_layout.addRow(QLabel('age:'),comb)
        spinb = QSpinBox()
        spinb.setValue(18)
        spinb.setRange(18,100)
        form_layout.addRow(QLabel('age:'), spinb)
        sex.addWidget(QRadioButton('male'))
        sex.addWidget(QRadioButton('female'))
        form_layout.addRow(QLabel('sex:'),sex)
        form_layout.addRow(QLabel('email:'),QLineEdit())
        form_layout.addRow(QLabel('address:'),QLineEdit())
        self.setTabText(1,'personal information')
        self.tab2.setLayout(form_layout)


    def initTab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('course'))
        layout.addWidget(QCheckBox('math'))
        layout.addWidget(QCheckBox('english'))
        self.setTabText(2,'course information')
        self.tab3.setLayout(layout)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = QTabWidgetDemo1()
    window.show()
    sys.exit(app.exec_())
