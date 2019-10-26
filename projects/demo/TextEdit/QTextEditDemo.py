#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/26 0026 19:52
#@Author  :    tb_youth
#@FileName:    QTextEditDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QTextEdit,QVBoxLayout

class TextEditDemo(QWidget):
    def __init__(self):
        super(TextEditDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('TextEditDemo')

        self.text_edit = QTextEdit()
        self.button_text = QPushButton('显示文本')
        self.button_html = QPushButton('显示HTML')
        self.button_toText = QPushButton('获取文本')
        self.button_toHtml= QPushButton('获取HTML')

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button_text)
        layout.addWidget(self.button_html)
        layout.addWidget(self.button_toText)
        layout.addWidget(self.button_toHtml)
        self.setLayout(layout)

        self.button_text.clicked.connect(self.onClickButtonText)
        self.button_html.clicked.connect(self.onClickButtonHtml)
        self.button_toText.clicked.connect(self.getText)
        self.button_toHtml.clicked.connect(self.getHtml)

    def onClickButtonText(self):
         self.text_edit.setPlainText('Hello World.....')

    def onClickButtonHtml(self):
        self.text_edit.setHtml('<font color = "red" size = "5"> Hello World!!</font>')

    def getText(self):
        print('获取的文本为：',self.text_edit.toPlainText())

    def getHtml(self):
        print('获取的HTML为：',self.text_edit.toHtml())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextEditDemo()
    window.show()
    sys.exit(app.exec_())







