#! -*- coding:utf-8 -*-
from scapy.all import *
import sys
ip=IP(dst='192.168.0.103',ttl=52)
# tcp=TCP(dport=80,flags="S",options=[('Length', 4), ('MSS', 1460)])
tcp=TCP(dport=135,flags="S")
pkt=ip/tcp
newpkt=IP(raw(pkt))
newpkt['TCP'].window=1024
newpkt.show2()
recv=sr1(newpkt,timeout=2,retry=1,verbose = False)