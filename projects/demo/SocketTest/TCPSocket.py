#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/2/8 0008 23:24
#@Author  :    tb_youth
#@FileName:    TCPSocket.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import socket

#创建一个socket：
'''
AF_INET:IPv4协议
AF_INET6:IPv6协议
SOCK_STREAM:面向流的TCP协议
'''
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
'''
（IP地址或域名，端口号)
'''
s.connect(('www.sina.com',80))

#发送数据
s.send(b'GET /HTTP/1.1\r\n www.sina.com\r\nConnection:close\r\n\r\n')

#接收数据
buffer = []

while True:
    #每次接收2k
    d = s.recv(2048)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
#关闭连接
s.close()
print(data)





