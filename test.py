#! -*- coding:utf-8 -*-
from scapy.all import *
import sys
import threading

dip='192.168.0.113'
startp=1
endp=200
t_num=2    #线程数
open=[]
close=[]
ip=IP(dst=dip)
tcp = TCP(dport=172, flags="S")
pkt = ip / tcp
# pkt=IP(raw(pkt))
# pkt.show()
recv=sr1(pkt,timeout=1)
recv.show()



