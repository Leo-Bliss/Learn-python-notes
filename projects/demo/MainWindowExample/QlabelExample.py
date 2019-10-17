#!/usr/bin/env python
# -*- coding:utf-8 -*-

# #Qlabel相关方法
# '''
# setAlignment():设置对齐方式
# setIndent():设置文本缩进
# text():获取文本内容
# setBuddy():设置伙伴关系
# setText():设置文本内容
# selectedText():返回所选字符
# setWordWrap():是否允许换行
# QLabel常用信号（事件）：
# 1.当鼠标滑过QLabel触发：linkHovered
# 2.当鼠标单击QLabel触发：linkActivated
# '''

import sys
from PyQt5.QtWidgets import QLabel,QApplication,QPushButton,QWidget,QVBoxLayout
from PyQt5.QtGui import QIcon,QPalette,QPixmap
#QPalette :调色板
from PyQt5.QtCore import Qt

#此时如果继承QMainWindow,此时label排版将出现问题，显示不全label中信息

class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.init_UI()
    def init_UI(self):
        self.resize(660,660)
        self.setWindowTitle('QLabelExample')
        self.setWindowIcon(QIcon('./photos/qq.png'))

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=white>文本标签</font>')
        label1.setAutoFillBackground(True)
        palette1 = QPalette()
        palette1.setColor(QPalette.Window,Qt.red)
        label1.setPalette(palette1)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>what?</a>")
        label2.setAlignment(Qt.AlignCenter)
        label2.linkHovered.connect(self.linkHovered)

        label3.setToolTip('图片')
        label3.setPixmap(QPixmap('./photos/qq.png'))
        label3.setAlignment(Qt.AlignCenter)


        label4.setText("<a href='http://www.baidu.com'>找度娘</a>")
        label4.setToolTip('baidu')
        label4.setAlignment(Qt.AlignRight)
        label4.linkActivated.connect(self.linkClicked)

        button1 = QPushButton('点我')
        button1.setToolTip('hahahah')
       # button1.setLocale()
        button1.setFixedSize(150,40)
        button1.setStyleSheet("QPushButton{color:black}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:rgb(80,255,255)}"
                                  #"QPushBUtton{background-image: url(:\demo\MainWindowExample\photos\space.png)}"
                                  "QPushButton{border:1px}"
                                  "QPushButton{border-radius:8px}")
        # button1.setIconSize(button1.size())
        #button1.setIcon(QIcon('./photos/space.png'))
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
