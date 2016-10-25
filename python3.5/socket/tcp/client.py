#!/usr/bin/env python
# encoding: utf-8

from socket import *

HOST = 'localhost'
PORT = 21563
BUFSIZ = 1024
ADDR=(HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    data = input('> ')
    if not data:
        break
    #str类型的内容发送不出去,只能是byte类型的
    tcpCliSock.send(bytes(data,encoding="utf-8"))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()

