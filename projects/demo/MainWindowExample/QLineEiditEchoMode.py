#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
QLineEdit控件回显模式

基本功能 ： 输入单行文本
EchoMode(回显模式)

4种回显：
1. Normal
2.NoEcho
3.Password
4.PasswordEchoOnEdit
'''
from PyQt5.QtWidgets import QApplication,QMessageBox,QMainWindow,QWidget
from PyQt5.QtWidgets import QLineEdit,QFormLayout,QPushButton,QHBoxLayout,QSizePolicy
from PyQt5.QtGui import QIcon
import  sys
class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QLineEdit回显')
        self.resize(605,240)
        self.setMaximumSize(605,240)
        self.setMinimumSize(605,240)
        self.setWindowIcon(QIcon('./photos/qq.png'))

        #LineEdit
        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        # PushButton
        btnOK = QPushButton('OK')
        btnCancel = QPushButton('Cancel')
        hBoxLayout = QHBoxLayout()
        hBoxLayout.addWidget(btnOK)
        hBoxLayout.addWidget(btnCancel)
        btnOK.clicked.connect(self.onClick_OKButton)
        # btnOK.setSizePolicy(QSizePolicy.Expanding,1)
        # btnCancel.setSizePolicy(QSizePolicy.Expanding,1)

        formLayout = QFormLayout()
        formLayout.addRow('normal',normalLineEdit)
        formLayout.addRow('noEcho',noEchoLineEdit)
        formLayout.addRow('password',passwordLineEdit)
        formLayout.addRow('passwordEchoOnEdit',passwordEchoOnEditLineEdit)
        formLayout.addRow(hBoxLayout)

        # ToolTip
        normalLineEdit.setToolTip('正常显示')
        noEchoLineEdit.setToolTip('输入不回显')
        passwordLineEdit.setToolTip('密码隐藏显示')
        passwordEchoOnEditLineEdit.setToolTip('输入时正常显示，移走光标隐藏')

        self.setLayout(formLayout)

        #PlaceholderText
        normalLineEdit.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwordLineEdit.setPlaceholderText('password')
        passwordEchoOnEditLineEdit.setPlaceholderText('passwordEchoOnEdit')

        #EchoMode
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

    def onClick_OKButton(self):
        print('OK被单击')
        # normal_data = self.







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditEchoMode()
    window.show()
    sys.exit(app.exec_())
