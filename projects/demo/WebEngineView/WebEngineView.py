#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/10 0010 23:14
#@Author  :    tb_youth
#@FileName:    WebEngineView.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys
import os

class WebEngnieViewDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('打开外部网页')
        self.setGeometry(5,50,1335,730)
        self.browser = QWebEngineView()
        #在线html页面
        # self.url = QUrl(r"https://www.csdn.net/")
        # self.browser.load(self.url)

        #本地html页面
        url = os.getcwd() + '/index4.html'
        self.browser.load(QUrl.fromLocalFile(url))

        #直接嵌入html页面
        self.browser.setHtml('''
                <!DOCTYPE html>
                <html>
                <head>
                <title>My fourth html</title>
                </head>
                <body>
                <style>
                body{
                background-color:lightblue;
                }
                #myHead{
                color:red;
                }
                .intro{
                background:pink;
                }
                .special{
                color:blue;
                }
                .myFooter{
                background-color:black;
                color:grey;
                }
                </style>
                <!--classes-->
                <!--class css use .xxx,but id use #xxx-->
                <h1 id="myHead">My home page</h1>
                <p class="intro special">My paragraph</p>''')
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebEngnieViewDemo()
    window.show()
    sys.exit(app.exec_())