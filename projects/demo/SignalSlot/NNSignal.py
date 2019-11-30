#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/30 0030 12:48
#@Author  :    tb_youth
#@FileName:    NNSignal.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

from PyQt5.QtCore import *

class NNSignal(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)

    def __init__(self):
        super(NNSignal,self).__init__()
        self.signal1.connect(self.call1)
        self.signal1.connect(self.call11)
        self.signal2.connect(self.call1) #触发信号1，传入参数只是为了满足定义
        #解除关联
        self.signal2.disconnect(self.call1)
        self.signal2.connect(self.call2)
        self.signal1.emit()
        self.signal2.emit(123)

    def call1(self):
        print('call1 emit')

    def call11(self):
        print('call11 emit')

    def call2(self,val):
        print('call2 emit:',val)


if __name__=='__main__':
    nn = NNSignal()