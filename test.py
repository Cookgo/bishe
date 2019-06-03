#! -*- coding:utf-8 -*-
from scapy.all import *
# count=0
# ip = '192.168.80.130'
# port = 801
# pkt = IP(dst=ip) / TCP(dport=port, flags='S')
#
# sr1(pkt, iface='VMware Virtual Ethernet Adapter for VMnet8',timeout=1)
#
def func():
    a=1
    print(id(a))
def func1():
    a=2
    print(id(a))

func()
func1()