#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/27 0027 12:11
#@Author  :    tb_youth
#@FileName:    CustomSignal1.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
信号与槽的连接
'''

from PyQt5.QtCore import pyqtSignal,pyqtSlot,QObject

class MyTypeSignal(QObject):
    #定义一个信号
    sendmsg = pyqtSignal(object)
    #发送3个参数的信号
    sendmsg1 = pyqtSignal(str,int,int)
    #传递list,dict
    sendmsg2 = pyqtSignal(list)
    sendmsg3 = pyqtSignal(dict)

    def run(self):
        self.sendmsg.emit("tbyouth 666")

    def run1(self):
        self.sendmsg1.emit("hhhhh",2,3)
    def run2(self):
        self.sendmsg2.emit([1,2,3])
    def run3(self):
        self.sendmsg3.emit({'a':123})



class MySlot(QObject):
    def get(self,msg):
        print("get : ",msg)

    def get1(self,msg,a,b):
        print('get1 : ',msg,a,b)

    def get2(self,lst):
        print(lst)
    def get3(self,dic):
        print(dic)


if __name__=='__main__':
    send = MyTypeSignal()
    slot = MySlot()

    send.sendmsg.connect(slot.get)
    send.sendmsg1.connect(slot.get1)
    send.sendmsg2.connect(slot.get2)
    send.sendmsg3.connect(slot.get3)

    send.run()
    send.run1()
    send.run2()
    send.run3()



