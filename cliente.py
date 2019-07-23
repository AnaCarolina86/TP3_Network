#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Python 2.7

import socket
import sys
import struct
import argparse
from timeit import default_timer as timer

parser = argparse.ArgumentParser(description='Client do programa batalha naval.')
parser.add_argument('ip', metavar='ip', type=str, help='IP do server.')
parser.add_argument('port', metavar='port', type=int, help='Porta do server.')
args = parser.parse_args()

#variables in the game

HOST = args.ip
PORT = args.port
timeout = 10 #time in seconds
tcp = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        tcp = socket.socket(af, socktype, proto)
    except socket.error as msg:
        tcp = None
        continue
    try:
        tcp.connect(sa)
    except socket.error as msg:
        tcp.close()
        tcp = None
        continue
    break
if tcp is None:
    print 'Not possible open the socket'
    sys.exit(1)

while True:
        message = raw_input()
        #print("message: " + message)

        tcp.send(message) #the user sends the message

        #start = timer() #starting the timer, more than 6 seconds: error message
        msg_recebida = tcp.recv(1024) #receive server anwser
        #tcp.settimeout(timeout) #the timer ends

        print msg_recebida #print: server anwser 


tcp.close()
