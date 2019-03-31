#! -*- coding:utf-8 -*-
from scapy.all import *
import sys

def op(pkt):
    pkt1=pkt
    pkt1['TCP'].flags='R'

pkt=IP()/TCP(flags='S')
op(pkt)
pkt.show()
