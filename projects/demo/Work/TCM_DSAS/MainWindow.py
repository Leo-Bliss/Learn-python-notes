#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/25 0025 19:54
#@Author  :    tb_youth
#@FileName:    MainWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
主界面
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton
from PyQt5.QtWidgets import QListWidget,QListWidgetItem,QStackedWidget
from PyQt5.QtWidgets import QHBoxLayout,QSizePolicy
from PyQt5.QtGui import QIcon,QPixmap,QPalette,QBrush

from projects.demo.Work.TCM_DSAS import InputWindow as IW
from projects.demo.Work.TCM_DSAS import SelectionWindow as SW

class MainWindowDemo(QWidget):
    def __init__(self):
        super(MainWindowDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(450,100,1000,800)
        self.setWindowTitle('中医药数据特征选择分析平台')

        self.list_widget = QListWidget()
        self.item_list = ['平台首页','数据导入','特征选择','数据分析','数据中心','算法中心','知识中心','联系作者']
        self.list_widget.addItems(self.item_list)
        item1 = QListWidgetItem()
        self.list_widget.addItem(item1)
        # quit = QLabel('退出')
        # quit.setPixmap(QPixmap('./image/退出.png'))

        # quit = QPushButton('退出')
        # quit.setMaximumSize(80, 50)
        # quit.setIcon(QIcon(QPixmap('./image/退出.png')))
        # quit.clicked.connect(self.close)

        # sizePolicy = QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        # # print(quit.size())
        # quit.setSizePolicy(sizePolicy)
        # self.list_widget.setItemWidget(item1,quit)

        #设置item间隔
        self.list_widget.setSpacing(5)

        #创建各个功能子窗口
        self.interface_widget = QWidget()
        self.input_widget = IW.InputWindowDemo()
        self.select_feature_widget = SW.SelectionWindowdemo()
        self.analyze_data_widget = QWidget()
        self.database_widget = QWidget()
        self.algorithm_widget = QWidget()
        self.konwledge_widget = QWidget()
        self.contact_widget = QWidget()

        #将各个功能子窗口压入栈窗口
        self.stack_widget = QStackedWidget()
        self.stack_widget.addWidget(self.interface_widget)
        self.stack_widget.addWidget(self.input_widget)
        self.stack_widget.addWidget(self.select_feature_widget)
        self.stack_widget.addWidget(self.analyze_data_widget)
        self.stack_widget.addWidget(self.database_widget)
        self.stack_widget.addWidget(self.algorithm_widget)
        self.stack_widget.addWidget(self.konwledge_widget)
        self.stack_widget.addWidget(self.contact_widget)

        #布局
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.list_widget)
        hlayout.addWidget(self.stack_widget)
        size_policy1 = self.list_widget.sizePolicy()
        size_policy2 = self.stack_widget.sizePolicy()
        size_policy1.setHorizontalPolicy(1)
        size_policy2.setHorizontalPolicy(9)
        self.list_widget.setSizePolicy(size_policy1)
        self.stack_widget.setSizePolicy(size_policy2)
        self.setLayout(hlayout)

        #美化:
        #去边框
        self.list_widget.setFrameShape(False)
        #icon
        self.setWindowIcon(QIcon('./image/分析.png'))
        #背景图片
        # palette = QPalette()
        # pix = QPixmap(r'./')
        # pix.scaled(self.width(),self.height())
        # palette.setBrush(QPalette.Background,QBrush(pix))
        # self.setPalette(palette)

        #关联单击信号
        self.list_widget.currentRowChanged.connect(self.onClickedListWidget)
        #导入数据窗口与特征选择窗口信号与槽关联，用于传递导入的数据
        self.input_widget.send.sendmsg2.connect(self.select_feature_widget.slot.get2)

    #根据index切换功能子窗口
    def onClickedListWidget(self,index):
        print(index)
        if index == 2:
            pass
            # self.input_widget.send.run2()
        self.stack_widget.setCurrentIndex(index)










if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindowDemo()
    window.show()
    sys.exit(app.exec_())