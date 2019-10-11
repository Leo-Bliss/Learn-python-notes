#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Qlabel相关方法
pydoc='''
setAlignment():设置对齐方式
setIndent():设置文本缩进
text():获取文本内容
setBuddy():设置伙伴关系
setText():设置文本内容
selectedText():返回所选字符
setWordWrap():是否允许换行
QLabel常用信号（事件）：
1.当鼠标滑过QLabel触发：linkHovered
2.当鼠标单击QLabel触发：linkActivated
'''
import sys
from PyQt5.QtWidgets import QLabel,QApplication,QMainWindow,QPushButton,QWidget,QVBoxLayout
from PyQt5.QtGui import QIcon,QFont,QPalette,QPixmap
#QPalette :调色板
from PyQt5.QtCore import Qt
class QLabelDemo(QMainWindow):
    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.init_UI()
    def init_UI(self):
        self.resize(660,660)
        self.setWindowTitle('QLabelExample。。。')
        self.status = self.statusBar()
        self.status.showMessage('status', 5000)
        self.setWindowIcon(QIcon('./photos/qq.png'))

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=yellow>文本标签</font>')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignLeft)

        label2.setText("<a href='#'>666666666666666</a>")
        label2.setAlignment(Qt.AlignCenter)
        label2.linkHovered.connect(self.linkHovered)

        label3.setText("<a href='http://www.baidu.com'>asssaa</a>")
        label3.setToolTip('baidu')
        label3.setAlignment(Qt.AlignRight)

        label4.setToolTip('photos')
        label4.setPixmap(QPixmap('./photos/qq.png'))
        label4.setAlignment(Qt.AlignAbsolute)
        label4.linkActivated.connect(self.linkClicked)

        button1 = QPushButton('点我')
        button1.setToolTip('hahahah')
        button1.clicked.connect(self.onClick_Button)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(button1)
        self.setLayout(vbox)

    def linkHovered(self):
        print('鼠标滑过label2触发')
    def linkClicked(self):
        print('鼠标单击label4触发')
    def onClick_Button(self):
        print('good night!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLabelDemo()
    window.show()
    sys.exit(app.exec_())
