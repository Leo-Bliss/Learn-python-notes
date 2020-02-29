#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/2/13 0013 14:26
#@Author  :    tb_youth
#@FileName:    TCP1.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import socket
import threading
import time


#服务端

def tcpLink(sock,addr):
    print('Accept new connection form %s:%s'%addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(b'Hello,%s!'%data.decode('utf-8').encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed'%addr)

if __name__=='__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定端口
    s.bind(('127.0.0.1',8888))
    #监听:参数为等待连接的最大数量
    s.listen(5)
    print('Waiting for connection...')
    while True:
        #接收一个新连接
        sock,addr = s.accept()
        #创建新线程赖处理TCP连接
        t = threading.Thread(target=tcpLink,args=(sock,addr))
        t.start()
