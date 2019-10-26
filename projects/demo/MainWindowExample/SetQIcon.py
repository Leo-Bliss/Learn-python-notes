#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget,QHBoxLayout,QMainWindow,QDesktopWidget
from PyQt5.QtGui import QIcon
class SetQIconFrame(QMainWindow):
   def __init__(self):
       super(SetQIconFrame, self).__init__()
       self.init_UI()

   def init_UI(self):
       #title
       self.setWindowTitle('QQ')
       #size
       self.resize(516,414)
       self.setMinimumSize(516,414)
       self.setMaximumSize(516,414)
       #status
       self.status = self.statusBar()
       self.status.showMessage('状态栏',5000)
       #window Icon
       self.setWindowIcon(QIcon('./photos/qq.png'))
       self.button1 = QPushButton('quit')
       #layout
       layout = QHBoxLayout()
       layout.addWidget(self.button1)
       #frame
       frame = QWidget()
       frame.setLayout(layout)
       self.setCentralWidget(frame)
       #connect
       self.button1.clicked.connect(self.onClick_button)

   def onClick_button(self):
       sender = self.sender()
       print(self.button1.text()+'被单击：退出app')
       app = QApplication.instance()
       app.quit()

   def center(self):
       screen = QDesktopWidget.screenGeometry()
       size = self.geometry()
       new_left = (screen.width()-size.width())//2
       new_top = (screen.height()-size.height())//2
       self.move(new_left,new_top())

if __name__=='__main__':
    app = QApplication(sys.argv)
    #app Icon:调用窗口Icon的方法
    #app.setWindowIcon(QIcon('./photos/qq.png'))
    window = SetQIconFrame()
    window.show()
    sys.exit(app.exec_())



