#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/2/8 0008 23:33
#@Author  :    tb_youth
#@FileName:    PortScanner.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
编写简单的客户端程序，
目标站点：119.29.231.174：22
此例子可用于端口扫描
'''

import sys
import socket
class PortScanner():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def scan(self,host,port,data):
        self.s.connect((host,port))
        self.s.send(data.encode('ascii'))
        while True:
            buf = self.s.recv(1024)
            if not len(buf):
                break
            sys.stdout.write(buf.decode('ascii'))
        self.s.close()


if __name__=='__main__':
    host = "119.29.231.174"
    port = 22
    data = "123"
    p = PortScanner()
    p.scan(host,port,data)



