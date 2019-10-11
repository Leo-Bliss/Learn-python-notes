#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,datetime
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QHBoxLayout,QPushButton,QToolTip
from PyQt5.QtGui import QIcon,QFont
# def get_week_day(s):
#     week_dict = {
#         1:'星期一',
#         2:'星期二',
#         3:'星期三',
#         4:'星期四',
#         5:'星期五',
#         6:'星期六',
#         7:'星期天'
#     }
#     return week_dict.get(s)
class ToolTipFrame(QMainWindow):
    def __init__(self):
        super(ToolTipFrame,self).__init__()
        self.init_UI()
    def init_UI(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        #%w:有时不是数字，why？
        # day = datetime.datetime.now().strftime('%w')
        # print(get_week_day(int(day)))
        #%a:英文简写
        e_day = day = datetime.datetime.now().strftime('%A')
        #(now_time,e_day)
        self.setToolTip('Today is %s <b>%s</b>'%(now_time,e_day))
        self.setGeometry(600, 400, 400, 400)
        self.setWindowTitle('QQ')
        self.resize(516,414)
        self.setMinimumSize(516,414)
        self.setMaximumSize(516,414)
        self.status = self.statusBar()
        self.status.showMessage('status',5000)
        #添加按钮
        self.button1 = QPushButton('quit')
        #布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        #框架
        frame = QWidget()
        frame.setLayout(layout)
        self.setCentralWidget(frame)
        #绑定
        self.button1.clicked.connect(self.onClick_Button)
        #设置提示信息
        self.button1.setToolTip('quit按钮')

    def onClick_Button(self):
        #sender = self.sender()
        print(self.button1.text()+'被单击')
        #app = QApplication(sys.argv)
        app = QApplication.instance()
        app.quit()

'''
想法：
界面提示：当地时间，天气等信息
'''

if __name__=='__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./photos/qq.png'))
    window = ToolTipFrame()
    window.show()
    sys.exit(app.exec_())


