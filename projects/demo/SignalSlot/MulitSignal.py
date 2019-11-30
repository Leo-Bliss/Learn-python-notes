#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/29 0029 22:16
#@Author  :    tb_youth
#@FileName:    MulitSignal.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
为类添加多个信号
'''

from PyQt5.QtCore import pyqtSlot,pyqtSignal,QObject

class MulitSignalDemo(QObject):
    signal1 = pyqtSignal()

    signal2 = pyqtSignal(int)

    signal3 = pyqtSignal(int,str)

    signal4 = pyqtSignal(list)

    signal5 = pyqtSignal(dict)

    #声明一个重载版本的信号
    #也就是槽函数的参数可以是int和str类型，也可以是只有str类型
    signal6 = pyqtSignal([int,str],[str])

    def __init__(self):
        super(MulitSignalDemo,self).__init__()
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        #self.signal6.connect(self.signalCall6)
        self.signal6[str].connect(self.signalCall6Overload)
        self.signal6[int,str].connect(self.signalCall6)

        self.signal1.emit()
        self.signal2.emit(10)
        self.signal3.emit(1,'hello')
        self.signal4.emit([1,2,3])
        self.signal5.emit({'name':'tbyout'})
        #self.signal6.emit(20,'test')
        self.signal6[str].emit('test2')
        self.signal6[int,str].emit(123,'ac')


    def signalCall1(self):
        print('signal1 emit')

    def signalCall2(self,val):
        print('signal2 emit,value:',str(val))

    def signalCall3(self,val,text):
        print('signal3 emit,value:',val,text)

    def signalCall4(self,lst):
        print('signal4 emit,value:',lst)

    def signalCall5(self,dct):
        print('signal5 emit,value:',dct)

    def signalCall6(self,val,text):
        print('signal6 emit,value',val,text)

    def signalCall6Overload(self,val):
        print('signal6 overload emit.value:',val)



if __name__=='__main__':
    mulit = MulitSignalDemo()
