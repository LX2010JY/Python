#!/usr/bin/env python
#encoding: utf-8

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 2300
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpCliSocket = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input('>')
    if not data:
        break
    udpCliSocket.sendto(bytes(data,encoding="utf8"),ADDR)
    data,ADDR = udpCliSocket.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode('utf8'))
udpCliSocket.close()


