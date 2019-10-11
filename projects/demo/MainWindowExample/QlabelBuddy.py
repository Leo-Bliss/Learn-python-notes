#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
QLable 与伙伴关系

'''
import sys
from PyQt5.QtWidgets import QApplication,QDialog,QPushButton,QLabel,QLineEdit,QGridLayout,QVBoxLayout,QMessageBox
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt

class QLabelBuddy(QDialog):
    def __init__(self):
        super(QLabelBuddy,self).__init__()
        self.init_UI()
    def init_UI(self):
        # self.resize(516, 414)
        # self.setMinimumSize(516, 414)
        # self.setMaximumSize(516, 414)
        self.setWindowTitle('QQ')
        self.setWindowIcon(QIcon('./photos/qq.png'))

        avatarLabel = QLabel()
        #avatarLabel.setFixedSize(100,100)
        avatarLabel.setPixmap(QPixmap('./photos/qq.png'))
        avatarLabel.setAlignment(Qt.AlignCenter)

        IDLable = QLabel('&ID:')
        IDLable.setToolTip('输入账号')
        self.IDLableEdit = QLineEdit()
        #设置伙伴关系，按alt加特定字母切换输入焦点
        IDLable.setBuddy(self.IDLableEdit)

        PWLable = QLabel('&PassWord:')
        PWLable.setToolTip('输入密码')
        self.PWLabelEdit = QLineEdit()
        #输入加密
        self.PWLabelEdit.setEchoMode(QLineEdit.Password)
        PWLable.setBuddy(self.PWLabelEdit)

        btnOK = QPushButton('&OK')
        btnOK.setStyleSheet("QPushButton {color:black}"
                            "QPushButton:hover {color:red}"
                            "QPushButton{background-color:blue}")
        btnCancel = QPushButton('&Cancel')
        btnCancel.setStyleSheet("QPushButton {color:black}"
                            "QPushButton:hover {color:yellow}"
                            "QPushButton{background-color:blue}")
        layout = QGridLayout(self)
        layout.addWidget(IDLable,0,0)
        layout.addWidget(self.IDLableEdit,0,1,1,2)#(1,2)-->占用一行两列
        layout.addWidget(PWLable,1,0)
        layout.addWidget(self.PWLabelEdit,1,1,1,2)
        layout.addWidget(btnOK,2,1)
        layout.addWidget(btnCancel,2,2)

        #Vlayout = QVBoxLayout(self)
        # Vlayout.addWidget(avatarLabel)
        # Vlayout.addLayout(layout)

        btnOK.clicked.connect(self.onClick_button)
        btnCancel.clicked.connect(self.link_button)
    def onClick_button(self):
        #合法性检验
        id = self.IDLableEdit.text()
        password = self.PWLabelEdit.text()
        #print(id,password)
        if(id==''or password==''):
            QMessageBox.warning(QDialog(),'警告','账号密码不能为空！')
            if id == '':
                self.IDLableEdit.setFocus()
                return
            if password == '':
                self.PWLabelEdit.setFocus()
        else:
            print('login...')

    def link_button(self):
        self.PWLabelEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLabelBuddy()
    window.show()
    sys.exit(app.exec_())






