#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import socket
import nmap

nm = nmap.PortScanner()
host='127.0.0.1'
nm.scan(host, '1-100 ')
# print("tcp")
tcpport=nm[host].all_tcp()
udpport=nm[host].all_udp()
print("tcp")
for tcp in tcpport:
    if nm[host]['tcp'][tcp]['state']=='open':
        print('%s'%tcp+' '+nm[host]['tcp'][tcp]['name']+' '+nm[host]['tcp'][tcp]['product']+' '+nm[host]['tcp'][tcp]['version'])
print("udp")
for udp in udpport:
    if nm[host]['udp'][udp]['state']=='open':
        print('%s'%udp+','+nm[host]['udp'][udp]['name']+' '+nm[host]['udp'][udp]['product']+' '+nm[host]['udp'][udp]['version'])

print(type(nm[host]['tcp'][21]['version']))


