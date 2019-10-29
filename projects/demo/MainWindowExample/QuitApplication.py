#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QHBoxLayout,QDesktopWidget,QApplication,QMainWindow,QWidget,QPushButton
from PyQt5.QtGui import QIcon
class QuickApplication(QMainWindow):
    def __init__(self):
        super(QuickApplication, self).__init__()
        #set windows title
        self.setWindowTitle('QuickAppliction')
        #set window size
        self.resize(516,414)
        self.setMinimumSize(516,414)
        self.setMaximumSize(516,414)
        #set statusBar
        self.status = self.statusBar()
        self.status.showMessage('Quit',5000)
        #add Button
        self.button1 = QPushButton('退出')
        #connect
        self.button1.clicked.connect(self.onCilck_Button)
        #layout
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        #frame
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)
    #set center form
    def ceneter(self):
        screen = QDesktopWidget.screenGeometry()
        size = self.geometry()
        new_left = (screen.width()-size.width())/2
        new_top = (screen.height()-size.height())/2
        self.move(new_left,new_top)
    #slot：quit
    def onCilck_Button(self):
        app = QApplication(sys.argv)
        now = SetQIcon.SetQIconFrame()
        now.show()
        sys.exit(app.exec_())

        # sender = self.sender()
        # print(sender.text()+'按钮被按下')
        # app = QApplication.instance()
        # app.quit()

if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = QuickApplication()
        # window.setWindowIcon(QIcon('./photos/qq.png'))
        window.show()
        sys.exit(app.exec_())