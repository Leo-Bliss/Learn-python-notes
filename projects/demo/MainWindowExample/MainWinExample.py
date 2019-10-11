#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout
from PyQt5.QtGui import QIcon
class MainWin(QMainWindow):
    #初始化
    def __init__(self,parent=None):
        super(MainWin,self).__init__(parent)
        #设置窗口标题
        self.setWindowTitle('QQ')

        #设置窗口大小
        self.resize(536,414)
        #固定窗口大小
        self.setMaximumSize(536,414)
        self.setMinimumSize(536,414)

        #左下角状态栏
        self.status = self.statusBar()
        #设置状态消息停留5ms
        self.status.showMessage('我是状态栏',5000)

        #退出程序


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./photos/qq.png'))
    window = MainWin()
    window.show()
    sys.exit(app.exec_())

