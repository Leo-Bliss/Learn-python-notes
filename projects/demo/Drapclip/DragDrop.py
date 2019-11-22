#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    15:07  2019/11/22
#@Author  :    tb_youth
#@FileName:    DragDrop.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
让控件支持拖拽
A.setDragEnabled(True)
B.setAcceptDrops(True)

B需要两个事件:
1.dragEnterEven 将A拖到B触发
2.dropEvent     在B的区域放下A时触发
'''


import sys
from PyQt5.QtWidgets import QApplication,QWidget,QComboBox,QFormLayout,QLabel,QLineEdit

class MyComBox(QComboBox):
    def __init__(self):
        super(MyComBox,self).__init__()
        self.setAcceptDrops(True)


    def dragEnterEvent(self,e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e):
        self.addItem(e.mimeData().text())


class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('拖拽操作')
        formlayout = QFormLayout()
        formlayout.addRow(QLabel('将左边的文本拖拽到右边的下拉列表中'))

        line_edit = QLineEdit()
        line_edit.setDragEnabled(True)

        combox = MyComBox()
        formlayout.addRow(line_edit, combox)
        self.setLayout(formlayout)


if __name__=='__main__':
    app =QApplication(sys.argv)
    window = DrapDropDemo()
    window.show()
    sys.exit(app.exec_())