#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/3/5 0005 20:39
#@Author  :    tb_youth
#@FileName:    SetParametersDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
集成设置变量和设置参数面板
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QDialog
from PyQt5.QtWidgets import QTabWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtGui import QIcon

import ParameterTabWidgeDemo
import VarTabWidgetDemo

#自定义的信号类，用于窗口通信
class MySignal(QObject):
    sender = pyqtSignal(dict)
    def send(self,parameter_dict):
        self.sender.emit(parameter_dict)



class PramaeterTabWidget(QTabWidget):
    def __init__(self,id,var_list):
        super().__init__()
        self.initUI(id,var_list)

    def initUI(self,id,var_list):
        self.setWindowTitle('参数设置')
        self.resize(800,800)
        self.tab1 = VarTabWidgetDemo.VarTabWidgetDemo(var_list)


        self.tab2 = self.getParamerterWindget(id)
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.addTab(self.tab1,'选项卡1')
        self.addTab(self.tab2,'选项卡2')
        self.addTab(self.tab3,'选项卡3')
        self.addTab(self.tab4,'选项卡4')

    def getParamerterWindget(self,id):
        if id == 0:
            return  ParameterTabWidgeDemo.Widget0()
        elif id == 1:
            return  ParameterTabWidgeDemo.Widget1()

class SetParameterDemo(QDialog):
    def __init__(self,id,var_list):
        super().__init__()
        self.initUI(id,var_list)

    def initUI(self,id,var_list):
        self.setWindowTitle('参数设置')
        self.setWindowIcon(QIcon('./image/参数.png'))
        self.resize(600,500)
        self.tab_widegt = PramaeterTabWidget(id,var_list)
        self.ok_button = QPushButton('确定')
        self.cancel_button = QPushButton('取消')
        self.tip_label = QLabel()
        self.tip_label.setText('<font color=blue> 请设置好各选项卡中的相关参数再点确定哦！</font>')
        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(self.cancel_button)
        hlayout.addWidget(self.ok_button)
        hlayout.setStretch(1,1)
        hlayout.setStretch(2, 2)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.tab_widegt)
        vlayout.addWidget(self.tip_label)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
        self.sendSignal = MySignal()
        self.ok_button.clicked.connect(self.getParameters)




    def getParameters(self):
        var_dict = self.tab_widegt.tab1.getVarDict()
        pramater_dict = self.tab_widegt.tab2.getParameterDict()
        all_dict = {'var_dict':var_dict,'parameter_dict':pramater_dict}
        self.sendSignal.send(all_dict)
        self.close()


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = SetParameterDemo(0,['1','2','3'])
    window.show()
    sys.exit(app.exec_())
