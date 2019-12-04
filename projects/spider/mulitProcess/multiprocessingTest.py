# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# #@Time    :    2019/11/18 0018 21:55
# #@Author  :    tb_youth
# #@FileName:    multiprocessingTest.py
# #@SoftWare:    PyCharm
# #@Blog    :    https://blog.csdn.net/tb_youth
#
# '''
# 学习如何使用多进程
# '''
#
# from multiprocessing import Process,Pool
# import os
# import time
#
# def run_case(text):
#     print(i)
#     print('入参：{0}，当前进程号：{1}'.format(text, os.getpid()))
#     time.sleep(5)
#
#
# if __name__ == '__main__':
#     '''
#     #父进程用于启动子进程
#     print('当前是父进程，进程号：{0}'.format(os.getpid()))
#     s1 = time.time()
#     for i in range(5):
#         child = Process(target=run_case, args=(str(i),))
#         print('子进程启动.')
#         child.start()
#         # join()进行进程阻塞(阻塞主进程，不加则会主进程结束在调用子进程)
#         # 目的是进程同步
#         # 但是不应该放在这里，应该放在所有start后面去执行
#         # 否则效率可能不如单进程
#         child.join()
#     e1 = time.time()
#     print('time = {0}'.format(e1-s1))
#     print('进程结束.')
#     print('+------------------------+')
#
#     print('当前是父进程，进程号：{0}'.format(os.getpid()))
#     s2 = time.time()
#     lst = []
#     for i in range(5):
#         child = Process(target=run_case, args=(i,))
#         print('子进程启动.')
#         child.start()
#         lst.append(child)
#     # 多进程join()的正确写法
#     for child in lst:
#         child.join()
#     e2 = time.time()
#     print('time = {0}'.format(e2 - s2))
#     print('进程结束.')
#     '''
#     #进程池：Pool
#     # 默认值就是cpu核数:os.cpu_count()
#     pool = Pool(4)
#     #子进程用完并不关闭而是再放回进程池中等待分配任务
#     #当进程池中线程不够，要等到之前进程执行完毕才可获得
#     print('当前是父进程，进程号：{0}'.format(os.getpid()))
#     print('子进程开始.')
#     s3 = time.time()
#     for i in range(5):
#         pool.apply_async(run_case,args=(i,))
#         print(i)
#     pool.close()
#     pool.join()
#     e3 = time.time()
#     print('time = {0}'.format(e3-s3))
#     print('子进程结束')
#     print('父进程结束')
#
#     #进程间通信，可以使用Queue
#
#
#
#
#
#


# 如果有大量进程，则可以用进程池，批量添加
from datetime import datetime
from multiprocessing import Process,Pool
import os,time

def music(func,loop):

    for i in range(loop):
        print ("I was listening to %s. %s" %(func,time.ctime()))
        time.sleep(1)

def movie(func,loop):
    for i in range(loop):
        print ("I was at the %s! %s" %(func,time.ctime()))
        time.sleep(5)

if __name__ =='__main__': #执行主进程
    # 主进程
    print('这是主进程，进程编号：%d' % os.getpid())
    t_start = datetime.now()
    pool = Pool()
    for i in range(4): # CPU有几核，每次就取出几个进程
        pool.apply_async(music, args=('爱情买卖',1))
        pool.apply_async(music, args=('阿凡达',3))
    pool.close() # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    pool.join() # 对Pool对象调用join()方法会等待所有子进程执行完毕
    t_end = datetime.now()
    print('主进程用时：%d毫秒' % (t_end - t_start).microseconds)