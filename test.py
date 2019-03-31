#! -*- coding:utf-8 -*-
from scapy.all import *
import sys

dip='192.168.0.1'
startp=1
endp=2000
t_num=2    #线程数
open=[]
close=[]
ip=IP(dst=dip)
tcp = TCP(dport=startp, flags="S")
pkt = ip / tcp
times=int((endp-startp+1)/t_num)

def is_open(pkt,startp,endp):
    l=list(range(startp,endp))
    random.shuffle(l)
    for p in l:
        pkt['TCP'].dport=p
        pkt['TCP'].sport = random.randint(1000,10000)
        recv = sr1(pkt,verbose=0,timeout=1)
        if recv is None:
            print('filter')
        elif recv['TCP'].flags=='SA':
            lock.acquire()
            open.append(p)
            lock.release()
        elif recv['TCP'].flags=='RA':
            lock.acquire()
            close.append(p)
            lock.release()

is_open(pkt,startp,endp)
print(open)
print(close)



