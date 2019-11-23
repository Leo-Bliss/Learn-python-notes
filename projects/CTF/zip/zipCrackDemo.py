#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    11:22  2019/11/19
#@Author  :    tb_youth
#@FileName:    zipCrackDemo.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
破解用6位以内数字加密的zip
'''

from zipfile import ZipFile
'''
zipFile:
提供对zip文件的创建，读写,
追加，解压以及列出文件列表
'''

def createPasswordFile(n):
    left =  10 ** (n-1)
    right = 10 ** n
    with open('password.txt','w',encoding='utf-8') as f:
        for password in range(left,right):
            f.write(str(password)+'\n')

def extractFile(zipFile,password):
    try:
        '''
         extractall(path=None,members=None,pwd=None)
         path:指定解压后文件的位置
         member:(可选)，指定Zip中药解压的文件，
         这个文件名称必须是通过naelist()方法返回的子集
         pwd:指定Zip文件的解压密码
        '''
        zipFile.extractall(pwd = bytes(password,"utf-8"))
        print('解压密码为: %s'%password)
        return True
    except:
        # print(password)
        pass
    return False

def crackZip(path,n):
    createPasswordFile(n)
    zip_file = ZipFile(path,'r')
    # print(zip_file.namelist())
    f = open(r'./password.txt','r',encoding='utf-8')
    for line in f.readlines():
        password = line.strip('\n')
        guess = extractFile(zip_file,password)
        if guess == True:
            break
    f.close()


if __name__=='__main__':
    path = r'./test.zip'
    crackZip(path,6)



