#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Python 2.7
import socket
import struct
import sys
import string
import argparse
import operator
from random import *

parser = argparse.ArgumentParser(description='Servidor do programa de gerenciamento.')
parser.add_argument('port', metavar='port', type=int, help='Porta do servidor.')
args = parser.parse_args()

# Fonte: https://docs.python.org/2/library/socket.html
HOST = None #  IP address  Server
PORT = args.port # Server Port
tcp = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        tcp = socket.socket(af, socktype, proto)
    except socket.error as msg:
        tcp = None
        continue
    try:
        tcp.bind(sa)
        tcp.listen(1)
    except socket.error as msg:
        tcp.close()
        tcp = None
        continue
    break
if tcp is None:
    print 'Not possible open the socket'
    sys.exit(1)

#protocol variables

class User:
    def __init__(self, password):
        self.password = password
        self.files = dict()

users = dict()

while True:
    #Conecting with the client
    con, _ = tcp.accept()
    while True:
        
        con.settimeout(100)
        try:
            message = con.recv(1024)
        except socket.timeout:
            print >> sys.stderr, 'Time is out. Close the conection!'
            con.close()
            break

        message_parts = message.split()
        code = message_parts[0]
        login = message_parts[1]
        password = message_parts[2]
        if code == 'N':
            if login in users:
                con.send("N -1")
            else:
                users[login] = User(password)
                con.send("N 0")

        elif code == 'S':
            file_name = message_parts[3]
            content = message_parts[4]
            if login not in users:
                con.send("S -1")
                continue
            user = users[login]
            if  user.password != password:
                con.send("S -2")
                continue
            if file_name in user.files:
                con.send("S 1")
            else:
                con.send("S 0")
            user.files[file_name] = content

        elif code == 'R':
            file_name = message_parts[3]
            if login not in users:
                con.send("R -1")
                continue
            user = users[login]
            if user.password != password:
                con.send("R -2")
                continue
            if file_name not in user.files:
                con.send("R -3")
            else:
                con.send("R 0 " + user.files[file_name])

        else:
            if login not in users:
                con.send("L -1")
                continue
            user = users[login]
            if user.password != password:
                con.send("L -2")
                continue
            else:
            .files = " ".join(user.files.keys())
                con.send("L 0 " +.files)


#Close the conection with the Client
con.close()

