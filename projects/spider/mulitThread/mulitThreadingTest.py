#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/23 0023 10:59
#@Author  :    tb_youth
#@FileName:    mulitThreadingTest.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import threading
from time import ctime,sleep


def music(func,loop):
    for i in range(loop):
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def movie(func,loop):
    for i in range(loop):
        print ("I was at the %s! %s" %(func,ctime()))
        sleep(5)
#创建线程组
threads = []
#创建线程t1，添加到线程组，目标函数，以及传参
t1 = threading.Thread(target=music,args=('爱情买卖',1))
threads.append(t1)
#创建线程t1，添加到线程组
t2 = threading.Thread(target=movie,args=('阿凡达',1))
threads.append(t2)

if __name__ == '__main__':
    #启动线程
    for t in threads:
        t.start()
    #守护线程
    for t in threads:
    # join（）的作用是，等待每个线程终止。
        t.join()
    print ("all over %s" %ctime())

