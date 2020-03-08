#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/1/5 0005 3:39
#@Author  :    tb_youth
#@FileName:    MainWindow3.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth



import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout
from PyQt5.QtWidgets import QListWidget,QStackedWidget
from PyQt5.QtWidgets import QHBoxLayout,QStyleFactory
from PyQt5.QtGui import QIcon

import InputWindow as IW
import SelectionWindow as SW
# import DataCenterWindow
import ContactWindow
import AboutUSWindow
import HomeWindow



class MainWindowDemo(QWidget):
    def __init__(self):
        super(MainWindowDemo,self).__init__()
        self.initUI()
        QApplication.setStyle(QStyleFactory.keys()[2])

    def initUI(self):
        self.resize(1200,800)
        #self.setGeometry(450,100,1200,800)
        self.setWindowTitle('中医药数据特征选择分析平台')
        #无边框
        #self.setWindowFlag(Qt.FramelessWindowHint)

        self.list_widget = QListWidget()
        self.item_list = ['平台首页','数据导入','特征选择','数据中心','反馈建议','关于我们']
        self.list_widget.addItems(self.item_list)


        #设置item间隔
        self.list_widget.setSpacing(5)

        #创建各个功能子窗口
        self.home = HomeWindow.HomeWindow()
        self.input_widget = IW.InputWindowDemo()
        self.select_feature_widget = SW.SelectionWindowdemo()
        # self.analyze_data_widget = QWidget()
        self.database_widget = QWidget() #DataCenterWindow.DataCenterWindow()
        # self.algorithm_widget = QWidget()
        # self.konwledge_widget = QWidget()
        self.contact_widget = ContactWindow.ConcatWindow()
        self.about_widget = AboutUSWindow.AboutUSWindowDemo()

        #将各个功能子窗口压入栈窗口
        self.stack_widget = QStackedWidget()
        self.stack_widget.addWidget(self.home)
        self.stack_widget.addWidget(self.input_widget)
        self.stack_widget.addWidget(self.select_feature_widget)
        # self.stack_widget.addWidget(self.analyze_data_widget)
        self.stack_widget.addWidget(self.database_widget)
        #self.stack_widget.addWidget(self.algorithm_widget)
        #self.stack_widget.addWidget(self.konwledge_widget)
        self.stack_widget.addWidget(self.contact_widget)
        self.stack_widget.addWidget(self.about_widget)

        #布局
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.list_widget)
        hlayout.addWidget(self.stack_widget)
        #等比例划分布局
        hlayout.setStretch(0,1)
        hlayout.setStretch(1,5)
        hlayout.setSpacing(0)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.setStretch(0,1)
        vlayout.setStretch(1,15)
        self.setLayout(vlayout)

        #美化:
        #去边框
        self.list_widget.setFrameShape(False)
        #icon
        self.setWindowIcon(QIcon('./image/分析.png'))
        # self.label.setPixmap(QPixmap('./image/分析.png'))



        #关联单击信号
        self.list_widget.currentRowChanged.connect(self.onClickedListWidget)
        #导入数据窗口与特征选择窗口信号与槽关联，用于传递导入的数据
        self.home.user_button.clicked.connect(self.onClickedUserBuuton)
        # self.home.user_center.triggered.connect(self.onClickedUserBuuton)


    #根据index切换功能子窗口
    def onClickedListWidget(self,index):
        if index == 2:
                self.input_widget.data_view_tab.signal.sender.connect(self.select_feature_widget.getModel)
                self.input_widget.data_view_tab.signal.send(self.input_widget.data_view_tab.model)
        else:
            pass
        self.stack_widget.setCurrentIndex(index)


    def onClickedUserBuuton(self):
        x = self.pos().x() + self.size().width() - self.home.user_widget.width()
        y = self.pos().y() + 130
        self.home.user_widget.move(x, y)
        # 这里使用exec_,使对话框变为模态对话框
        self.home.user_widget.exec_()
        # self.home.user_widget.destroy()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindowDemo()
    window.show()
    sys.exit(app.exec_())
