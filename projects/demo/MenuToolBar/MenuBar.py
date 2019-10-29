#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/25 0025 21:41
#@Author  :    tb_youth
#@FileName:    MenuBar.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import  sys
from  PyQt5.QtWidgets import QApplication,QMainWindow,QTextEdit,QAction,QStatusBar
import os

class MenuBarDemo(QMainWindow):
    def __init__(self):
        super(MenuBarDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('MenuBarDemo')
        #获取菜单栏
        bar  = self.menuBar()
        #增加顶层菜单
        file = bar.addMenu('File')
        #子菜单
        file.addAction('new')

        open = QAction('open',self)
        open.setShortcut('Ctrl + o')
        file.addAction(open)
        save = QAction('save',self)
        save.setShortcut('Ctrl + s')
        file.addAction(save)

        edit = bar.addMenu('Edit')
        edit.addAction('copy')
        edit.addAction('paste')
        edit.addAction('cut')
        edit.addAction('clear')

        view = bar.addMenu('View')
        navigate = bar.addMenu('Navigate')

        about = bar.addMenu('About')
        about.addAction('help')

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        save.triggered.connect(self.click_save)

        file.triggered.connect(self.click)
        about.triggered.connect(self.click)
    def click(self,p):
        print(p.text())
        if p.text() == 'help':
            print('cpu数：',os.cpu_count())
            # 输出的内容nt代表windows操作系统 linux为posix
            system_dic = {'nt':'Windows','posix':'Linux'}
            print('操作系统名：%s'%system_dic.get(os.name))

            #路径下是否存在某个文件
            print('Bar.py存在') if os.path.exists('Bar.py') else print('Bar.py不存在')
            print('MenuBar.py存在') if os.path.exists('MenuBar.py') else print('MenuBar.py不存在')




    def click_save(self):
         msg = '%s启动：文件保存中...'%(self.sender().text())
         self.status.showMessage(msg,5000)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MenuBarDemo()
    window.show()
    sys.exit(app.exec_())




