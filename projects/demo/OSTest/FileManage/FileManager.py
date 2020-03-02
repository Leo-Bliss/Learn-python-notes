#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/3/2 0002 10:48
#@Author  :    tb_youth
#@FileName:    FileManager.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth


'''
需求：
忽略文件的格式后缀，将同名文件放到同名目录下，
同名目录需要根据文件名创建。
(批量处理)
'''

import os
import shutil

class FileManager:
    def __init__(self,src_dir):
        self.src_dir = src_dir

    def moveFiles(self):
        os.chdir(self.src_dir)
        for root,dirs,files in os.walk(os.getcwd()):
            print('root:',root)
            print('file:',files)
            print('dir:',dirs)
            print('-' * 100)
            '''
            文件在所在文件夹则不一移动，
            否则移动到创建的同名文件夹下
            '''
            for file in files:
                name = file.rsplit('.',maxsplit=1)[0]
                aim_dir = '{}\{}'.format(self.src_dir,name)
                # print(aim_dir)
                now_dir = '{}\{}'.format(root, file)
                try:
                    if not os.path.exists(aim_dir):
                        os.mkdir(aim_dir)
                except Exception as e:
                    print(e)
                if now_dir == aim_dir:
                    print('{}不需要移动'.format(now_dir))
                else:
                    try:
                        shutil.move(now_dir, aim_dir)
                        print('{}已经移动到了{}'.format(now_dir, aim_dir))
                    except:
                        pass

if __name__=='__main__':
    path = r'D:\ACM'
    m = FileManager(path)
    m.moveFiles()