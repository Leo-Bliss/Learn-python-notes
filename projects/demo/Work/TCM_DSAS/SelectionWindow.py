#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    15:43  2019/11/26
#@Author  :    tb_youth
#@FileName:    SelectionWindow.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
特征选择窗口：
有设置参数功能
'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QComboBox,QTextEdit,QLineEdit
from PyQt5.QtWidgets import QPushButton,QToolBar,QAction
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QIcon

class SelectionWindowdemo(QWidget):
    def __init__(self):
        super(SelectionWindowdemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('特征选择窗口')

        self.tool_bar = QToolBar()
        self.set_parameter = QAction(QIcon('./image/参数设置.png'),'设置参数',self)
        self.run = QAction(QIcon('./image/运行程序.png'),'运行程序',self)
        self.tool_bar.addAction(self.set_parameter)
        self.tool_bar.addAction(self.run)

        self.lable = QLabel('请选择算法:')
        self.comb1 = QComboBox()
        self.comb1.addItems(['FSFS','Lasso'])
        self.comb2 = QComboBox()
        self.comb2.addItems(['算法','内容'])
        self.line_edit = QLineEdit()
        self.button = QPushButton('搜索')

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.lable)
        hlayout.addWidget(self.comb1)
        hlayout.addWidget(self.tool_bar)
        hlayout.addWidget(self.comb2)
        hlayout.addWidget(self.line_edit)
        hlayout.addWidget(self.button)

        self.text_edit = QTextEdit()
        self.text_edit.setText('four steps for features selection:\nFliter,Semi_weapper,Union,Voting.')
        self.text_edit.setReadOnly(True)

        vlayout = QVBoxLayout()
        # vlayout.addWidget(self.tool_bar)
        vlayout.addItem(hlayout)
        vlayout.addWidget(self.text_edit)
        self.setLayout(vlayout)

        self.comb1.currentIndexChanged.connect(self.selectionChange)
        # self.comb2.currentIndexChanged(self.selecttionChange2)
        self.button.clicked.connect(self.clickSearch)


    def selectionChange1(self):
        if self.comb1.currentText() == 'FSFS':
            text = 'four steps for features selection:\nFliter,Semi_weapper,Union,Voting.'
            self.text_edit.setText(text)
        else:
            self.text_edit.setText(self.comb1.currentText())


    def clickSearch(self):
        text = self.line_edit.text()
        if self.comb2.currentText() == '算法':
            index = self.comb1.findText(text)
            if index != -1:
                self.comb.setCurrentIndex(index)
            else:
                print('没有找到{}'.format(text))
                print('没有找到{}'.format(text))
        else:
            pass








if __name__=='__main__':
    app = QApplication(sys.argv)
    window = SelectionWindowdemo()
    window.show()
    sys.exit(app.exec_())