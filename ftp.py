#! -*- coding:utf-8 -*-
from scapy.all import *
import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.80.130', 21))
temp=s.recv(1024)
temp=temp.decode()
print(temp)
usename="us"
send_buf="USER %s\r\n"%usename
s.send(send_buf.encode())
temp=s.recv(1024)
print(temp.decode())




