#! -*- coding:utf-8 -*-
from scapy.all import *
import sys
import threading

dip='192.168.80.130'
startp=1
endp=100
t_num=4   #线程数
open=set([])
close=set([])
filter=set([])
filter_temp=set([])
ip=IP(dst=dip)
tcp = TCP(dport=85, flags="S")
pkt = ip / tcp
# pkt=IP(raw(pkt))
times=int((endp-startp+1)/t_num)
t = []
lock = threading.Lock()

def one_tcp_open(pkt,port):
    pkt['TCP'].dport = port
    pkt['TCP'].sport = random.randint(1000, 10000)
    recv = sr1(pkt, verbose=0, timeout=1)
    if recv is None:
        lock.acquire()
        filter.add(port)
        lock.release()
    elif recv['TCP'].flags == 'SA':
        lock.acquire()
        open.add(port)
        lock.release()
        pktR = copy.deepcopy(pkt)
        pktR['TCP'].flags = 'R'
        sr1(pktR, verbose=0, timeout=0.1)
    elif recv['TCP'].flags == 'RA':
        lock.acquire()
        close.add(port)
        lock.release()

def is_tcp_open(pkt,startp,endp):
    l=list(range(startp,endp))
    random.shuffle(l)
    for p in l:
        one_tcp_open(pkt, p)
for i in range(t_num):

    pkt1=copy.deepcopy(pkt)
    t1=threading.Thread(target=is_tcp_open,args=(pkt1,startp+i*times,startp+(i+1)*times))
    t1.start()
    t.append(t1)
for i in range(t_num):
    t[i].join()
is_tcp_open(pkt,startp+t_num*times,endp)
for i in range(2):
    if len(close)<len(filter) or len(open)<len(filter):
        break
    if filter is not None:
        for p in filter:
            pkt['TCP'].dport = p
            pkt['TCP'].sport = random.randint(1000, 10000)
            recv = sr1(pkt, verbose=0, timeout=1)
            if recv is None:
                pass
            elif recv['TCP'].flags=='SA':
                filter_temp.add(p)
                open.add(p)
                pktR = copy.deepcopy(pkt)
                pktR['TCP'].flags = 'R'
                sr1(pktR, verbose=0, timeout=0.1)
            elif recv['TCP'].flags=='RA':
                filter_temp.add(p)
                close.add(p)
        for i in filter_temp:
            filter.remove(i)
        filter_temp = set([])
print(open)
print(close)
print(filter)



