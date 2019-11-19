#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/18 0018 21:55
#@Author  :    tb_youth
#@FileName:    multiprocessingTest.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
学习如何使用多进程
'''

from multiprocessing import Process,Pool
import os
import time

def run_case(text):
    print('入参：{0}，当前进程号：{1}'.format(text, os.getpid()))
    time.sleep(5)


if __name__ == '__main__':
    '''
    #父进程用于启动子进程
    print('当前是父进程，进程号：{0}'.format(os.getpid()))
    s1 = time.time()
    for i in range(5):
        child = Process(target=run_case, args=(str(i),))
        print('子进程启动.')
        child.start()
        # join()进行进程阻塞(阻塞主进程，不加则会主进程结束在调用子进程)
        # 目的是进程同步
        # 但是不应该放在这里，应该放在所有start后面去执行
        # 否则效率可能不如单进程
        child.join()
    e1 = time.time()
    print('time = {0}'.format(e1-s1))
    print('进程结束.')
    print('+------------------------+')

    print('当前是父进程，进程号：{0}'.format(os.getpid()))
    s2 = time.time()
    lst = []
    for i in range(5):
        child = Process(target=run_case, args=(i,))
        print('子进程启动.')
        child.start()
        lst.append(child)
    # 多进程join()的正确写法
    for child in lst:
        child.join()
    e2 = time.time()
    print('time = {0}'.format(e2 - s2))
    print('进程结束.')
    '''
    #进程池：Pool
    # 默认值就是cpu核数:os.cpu_count()
    pool = Pool(4)
    #子进程用完并不关闭而是再放回进程池中等待分配任务
    #当进程池中线程不够，要等到之前进程执行完毕才可获得
    print('当前是父进程，进程号：{0}'.format(os.getpid()))
    print('子进程开始.')
    s3 = time.time()
    for i in range(5):
        pool.apply_async(run_case,args=(i,))
        print(i)
    pool.close()
    pool.join()
    e3 = time.time()
    print('time = {0}'.format(e3-s3))
    print('子进程结束')
    print('父进程结束')

    #进程间通信，可以使用Queue






