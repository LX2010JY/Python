#!/usr/bin/env python
# encoding: utf-8

from socket import *
from time import ctime

HOST = ''
PORT = 21563
BUFSIZ = 1024
ADDR = (HOST,PORT)
tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
while True:
    print ('waitting for connection...')
    tcpCliSock,addr = tcpSerSock.accept()
    print ('connect from :',addr)
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        print(addr[0],':',addr[1],'> ',data.decode('utf8'))
        if not data:
            break
        tcpCliSock.send(bytes('[%s] %s'%(ctime(),data.decode('utf-8')),encoding='utf-8'))
    tcpCliSock.close()
tcpSerSock.close()
