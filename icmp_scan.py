#! -*- coding:utf-8 -*-
from scapy.all import *
icmp=IP(dst='192.168.1.4')/ICMP()
# icmp['IP'].len=1
icmp=IP(raw(icmp))
icmp.show()
s=sr1(icmp,timeout=1)