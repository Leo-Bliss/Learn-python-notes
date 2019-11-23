#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    15:38  2019/11/22
#@Author  :    tb_youth
#@FileName:    ClipBoard.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth


import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QMimeData

class ClipBoardDemo(QWidget):
    def __init__(self):
        super(ClipBoardDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('ClipBoardDemo')

        copy_text_button = QPushButton('复制文本')
        paste_text_button = QPushButton('粘贴文本')

        copy_html_button = QPushButton('复制HTML')
        paste_html_button = QPushButton('粘贴HTML')

        copy_image_button = QPushButton('复制图像')
        paste_image_button = QPushButton('粘贴图像')

        self.text_label = QLabel('tbyouth')
        self.image_label = QLabel()
        # self.image_label.setPixmap(QPixmap(r'./school1.png'))

        copy_text_button.clicked.connect(self.copyText)
        paste_text_button.clicked.connect(self.pasteText)
        copy_html_button.clicked.connect(self.copyHtml)
        paste_html_button.clicked.connect(self.pasteHtml)
        copy_image_button.clicked.connect(self.copyImage)
        paste_image_button.clicked.connect(self.pasteImage)

        grid_layout = QGridLayout()
        grid_layout.addWidget(copy_text_button,0,0)
        grid_layout.addWidget(copy_html_button,0,1)
        grid_layout.addWidget(copy_image_button,0,2)

        grid_layout.addWidget(paste_text_button, 1, 0)
        grid_layout.addWidget(paste_html_button, 1, 1)
        grid_layout.addWidget(paste_image_button,1, 2)

        grid_layout.addWidget(self.text_label,2,0,1,2)
        grid_layout.addWidget(self.image_label, 2,2)
        self.setLayout(grid_layout)


    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText('2333')

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.text_label.setText(clipboard.text())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap(r'./school1.png'))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.image_label.setPixmap(clipboard.pixmap())

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml:
            self.text_label.setText(mimeData.html())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClipBoardDemo()
    window.show()
    sys.exit(app.exec_())