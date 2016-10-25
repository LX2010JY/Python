#!/usr/bin/env python
#encoding: utf-8
from socket import *
from time import ctime

HOST = ''
PORT = 2300
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSocket = socket(AF_INET,SOCK_DGRAM)
udpSerSocket.bind(ADDR)

while True:
    print('waiting for message...')
    data,addr = udpSerSocket.recvfrom(BUFSIZ)
    udpSerSocket.sendto(bytes('[%s] %s'%(ctime(),data.decode('utf8')),encoding="utf8"),addr)
    print('> received from and return to:',addr)
udpSerSocket.close()