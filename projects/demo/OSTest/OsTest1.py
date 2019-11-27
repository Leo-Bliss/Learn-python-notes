#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/27 0027 23:43
#@Author  :    tb_youth
#@FileName:    OsTest1.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
测试os模块中的各个方法
'''
import os
import  sys


if __name__ == '__main__':
    #当前目录
    print(os.path.abspath('.'))
    #当前目录的另一种获取方法
    print(os.getcwd())

    # 当前目录父目录
    print(os.path.abspath('..'))

    #当前目录下该文件 工作目录(实质是拼接了一个文件名)
    print(os.path.abspath('OSTest1.py'))

    #目前这个文件的所在目录
    print(os.path.abspath(os.curdir))

    #改变当前目录
    # os.chdir('E:')
    # print(os.path.abspath('.'))

    #组合路径(去重的拼接)
    print(os.path.join('/home', '/home/file1/', '/home/file1/file2/'))

    print(os.walk(os.getcwd()))
    # for item in os.walk(os.getcwd()):
    #     print(item)

    #os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
    #top ：需要展示文件结构的目录
    #topdown：自上而下展示
    #oneerror：一个OSError实例，用于报告错误然后继续执行
    #followlinks：通过软链接访问目录
    #(dirpath, dirnames, filenames)
    #会逐层打印 当前根目录 当前根目录下的文件夹 当前根目录下的文件
    os.chdir('..')
    for root, dirs, files in os.walk(os.getcwd()):
        print(root, dirs, files)
        print('-' * 100)

    print(len(sys.path))
    #sys.path[0]为当前文件工作目录
    for item in sys.path:
        print(item)
