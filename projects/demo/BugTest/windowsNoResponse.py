#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    :    2020/2/29 0029 19:50
# @Author  :    tb_youth
# @FileName:    windowsNoResponse.py
# @SoftWare:    PyCharm
# @Blog    :    https://blog.csdn.net/tb_youth

'''
测试界面运行逻辑代码，界面出现无响应的bug
'''

from PyQt5.QtWidgets import QDialog, QApplication
# from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QPushButton, QLabel,QProgressBar
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer, QThread,pyqtSignal,QObject,pyqtSlot
import sys, time


class TimeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.start_btn = QPushButton("开始")
        self.stop_btn = QPushButton("停止")
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.start_btn)
        hlayout.addWidget(self.stop_btn)
        vlayout = QVBoxLayout()
        self.label = QLabel('####')
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.label)
        self.setLayout(vlayout)
        self.start_btn.clicked.connect(self.update)
        self.sec = 0

    def update(self):
        '''
        这样写虽然没有逻辑错误，
        但是一运行，就会出现界面卡死。
        这可能与python的GIL锁有关，
        time是python的库，而QT底层为C++的，
        time.sleep(1)后未将CPU控制权还给Qt
        :return:
        '''
        for i in range(10000):
            self.sec += 1
            self.label.setText(str(self.sec))
            time.sleep(1)
            #下面这种方法效果不好，不流畅
            # qApp.processEvents()


'''
        解决上述问题的方案1：
        使用QTimer类，即统一使用Qt
'''

class TimeDialog1(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.start_btn = QPushButton("开始")
        self.stop_btn = QPushButton("停止")
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.start_btn)
        hlayout.addWidget(self.stop_btn)
        vlayout = QVBoxLayout()
        self.label = QLabel('####')
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.label)
        self.setLayout(vlayout)

        self.sec = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.start_btn.clicked.connect(lambda: self.timer.start(1000))
        self.stop_btn.clicked.connect(lambda: self.timer.stop())

    def update(self):
        self.sec += 1
        self.label.setText(str(self.sec))


'''
      解决上述问题的方案2：
      开一个线程专门用于运行time.sleep
      （把它放到QThread）
'''

class MyThread(QThread):
    signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.sec = 0
    def __del__(self):
        self.wait()

    def run(self):
       while True:
            #发送信号后sleep一秒
            self.signal.emit(self.sec)
            self.sec += 1
            time.sleep(5)
            #QThread自身也有一个sleep方法
            # self.sleep(1)


class TimeDialog2(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.start_btn = QPushButton("开始")
        self.stop_btn = QPushButton("停止")
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.start_btn)
        hlayout.addWidget(self.stop_btn)
        vlayout = QVBoxLayout()
        self.label = QLabel('####')
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.label)
        self.setLayout(vlayout)
        thread = MyThread() #工作线程
        thread.signal.connect(self.update)
        self.start_btn.clicked.connect(lambda: thread.start())
        self.stop_btn.clicked.connect(lambda:thread.terminate())

    def update(self,sec):
        self.label.setText(str(sec))




'''
扩展方案：使用QObject类，
使用方法moveToThread将工作对象移到到QThread中运行
'''
class Worker(QObject):
    finished = pyqtSignal()
    int_signal = pyqtSignal(int)

    @pyqtSlot()
    def work(self):
        for i in range(1,101):
            time.sleep(0.15)
            #工作过程中发送数据
            self.int_signal.emit(i)

        #发送work完成信号
        self.finished.emit()

class TimeDialog3(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.start_btn = QPushButton("开始")
        self.stop_btn = QPushButton("停止")
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.start_btn)
        hlayout.addWidget(self.stop_btn)
        vlayout = QVBoxLayout()
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.progress_bar)
        self.setLayout(vlayout)

        self.worker = Worker()
        self.thread = QThread()
        self.worker.int_signal.connect(self.update)
        self.worker.finished.connect(self.thread.quit)
        self.thread.started.connect(self.worker.work)
        self.worker.moveToThread(self.thread)
        self.thread.start()



    def update(self,i):
        self.progress_bar.setValue(i)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = TimeDialog2()
    dialog.show()
    sys.exit(app.exec_())
