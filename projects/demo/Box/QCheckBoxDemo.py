#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/29 0029 22:31
#@Author  :    tb_youth
#@FileName:    QCheckBoxDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox,QWidget,QHBoxLayout
from PyQt5.QtCore import Qt

class CheckBoxDemo(QWidget):
    def __init__(self):
        super(CheckBoxDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(200,200)
        self.setWindowTitle('CheckBoxDemo')

        self.checkBox1 = QCheckBox('复选框控件1')
        #初始设置已选中
        self.checkBox1.setChecked(True)
        #关联信号
        self.checkBox1.stateChanged.connect(lambda: self.checkBoxStatus(self.checkBox1))
        # 默认未选中
        self.checkBox2 = QCheckBox('复选框控件2')
        self.checkBox2.stateChanged.connect(lambda: self.checkBoxStatus(self.checkBox2))


        self.checkBox3 = QCheckBox('半选中')
        #设置版选中
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect(lambda: self.checkBoxStatus(self.checkBox3))

        layout = QHBoxLayout()
        layout.addWidget(self.checkBox1)
        layout.addWidget(self.checkBox2)
        layout.addWidget(self.checkBox3)
        self.setLayout(layout)

    def checkBoxStatus(self,cb):
        print(cb.text(),cb.isChecked())
        check1Status = self.checkBox1.text()+' isChecked = '+str(self.checkBox1.isChecked())+',checkStatus = '+\
        str(self.checkBox1.checkState())+'\n'
        check2Status = self.checkBox2.text()+' isChecked = '+str(self.checkBox2.isChecked())+',checkStatus = '+\
        str(self.checkBox2.checkState())+'\n'
        check3Status = self.checkBox3.text() + ' isChecked = ' + str(self.checkBox3.isChecked()) + ',checkStatus = ' + \
                       str(self.checkBox3.checkState()) + '\n'
        print(check1Status,check2Status,check3Status)


if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = CheckBoxDemo()
    window.show()
    sys.exit(app.exec_())




