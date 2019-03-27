#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import socket
import nmap

# s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(10)
# s.bind(('127.0.0.1', 10000))
# result = s.connect_ex(('192.168.1.4', 445))
# print(result)
# if(result==0):
#     print("open")
# else:
#     print("nope")
nm = nmap.PortScanner()
host='127.0.0.1'
nm.scan(host, '1-1000')
# print("tcp")
tcpport=nm[host].all_tcp()
udpport=nm[host].all_udp()
print("tcp")
for tcp in tcpport:
    if nm[host]['tcp'][tcp]['state']=='open':
        print('%s'%tcp+','+nm[host]['tcp'][tcp]['name'])
print("udp")
for udp in udpport:
    if nm[host]['udp'][udp]['state']=='open':
        print('%s'%udp+','+nm[host]['udp'][udp]['name'])




