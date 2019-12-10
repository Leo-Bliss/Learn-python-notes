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
from projects.demo.Work.TCM_DSAS import SetParameterDialog
from projects.demo.Work.TCM_DSAS.algorithm import FSFS
from projects.demo.Work.TCM_DSAS.algorithm import Lasso
import os
from projects.demo.SignalSlot.CustomSignal1 import MySlot

class SelectionWindowdemo(QWidget):
    def __init__(self):
        super(SelectionWindowdemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('特征选择窗口')
        self.parameter_dict = None
        self.slot = MySlot()

        self.tool_bar = QToolBar()
        self.set_parameter = QAction(QIcon('./image/参数设置.png'),'设置参数',self)
        self.run = QAction(QIcon('./image/运行程序.png'),'运行程序',self)
        self.tool_bar.addAction(self.set_parameter)
        self.tool_bar.addAction(self.run)

        self.lable = QLabel('选择算法:')
        self.comb1 = QComboBox()
        self.comb1.addItems(['FSFS','Lasso'])
        # self.comb2 = QComboBox()
        # self.comb2.addItems(['算法','内容'])
        self.line_edit = QLineEdit()
        self.button = QPushButton('搜索')

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.lable)
        hlayout.addWidget(self.comb1)

        # hlayout.addWidget(self.comb2)
        hlayout.addWidget(self.line_edit)
        hlayout.addWidget(self.button)
        hlayout.addWidget(self.tool_bar)
        hlayout.addStretch(3)
        hlayout.setSpacing(10)

        self.text_edit = QTextEdit()
        self.text_edit.setText('Four steps for features selection:\nFliter,Semi_weapper,Union,Voting.')
        self.text_edit.setReadOnly(True)
        self.run.setEnabled(False)

        vlayout = QVBoxLayout()
        vlayout.addItem(hlayout)
        vlayout.addWidget(self.text_edit)
        self.setLayout(vlayout)

        self.comb1.currentIndexChanged.connect(self.selectionChange1)
        # self.comb2.currentIndexChanged(self.selecttionChange2)
        self.button.clicked.connect(self.clickSearch)
        self.set_parameter.triggered.connect(self.getParameter)
        self.run.triggered.connect(self.runProcess)

    #选择特征选择的算法
    def selectionChange1(self):
        if self.comb1.currentText() == 'FSFS':
            text = 'four steps for features selection:\nFliter,Semi_weapper,Union,Voting.'
            self.text_edit.setText(text)
        else:
            self.text_edit.setText(self.comb1.currentText())

    #搜索算法
    def clickSearch(self):
        text = self.line_edit.text()
        index = self.comb1.findText(text)
        if index != -1:
            self.comb1.setCurrentIndex(index)
        else:
            print('没有找到{}'.format(text))


    #获取参数对话框的相关参数
    def getParameter(self):
        self.dialog = SetParameterDialog.ParamerterDemo()
        self.dialog.signal.sender.connect(self.setParameter)
        self.dialog.show()

    #设置算法的参数
    def setParameter(self,dic):
         print(dic)
         self.parameter_dict = dic
         self.text_edit.setText(str(dic))
         self.run.setEnabled(True)

    def runProcess(self):
        file_name = 'data1.xlsx'
        path = '{0}\data\{1}'.format(os.path.abspath('.'), file_name)
        try:
            print('特征选择中...')
            f = FSFS.FSFSDemo(path,self.parameter_dict)
            res_list = f.run()
            str_res = ',\n'.join(res_list)
            res = '最终选择出的特征共{0}个:\n{1}'.format(len(res_list),str_res)
            self.text_edit.setText(res)
            print('特征选择完成！！！')
        except Exception as e:
            print(e)










if __name__=='__main__':
    app = QApplication(sys.argv)
    window = SelectionWindowdemo()
    window.show()
    sys.exit(app.exec_())