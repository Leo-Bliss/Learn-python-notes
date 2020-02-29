#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/2/13 0013 14:49
#@Author  :    tb_youth
#@FileName:    TCP2.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import socket

#客户端

if __name__=='__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #建立连接
    s.connect(('127.0.0.1',8888))
    #接收欢迎消息
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Mike',b'Bob',b'Joe']:
        #发送数据
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()