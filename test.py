#! -*- coding:utf-8 -*-
from scapy.all import *
count=0
ip = '192.168.80.130'
port = 21
pkt = IP(dst=ip) / TCP(dport=port, flags='S')

send(pkt, iface='VMware Virtual Ethernet Adapter for VMnet8')
str = 'ip src ' + ip + ' and tcp port ' + str(port)
print(str)
# pkts = sniff(iface='VMware Virtual Ethernet Adapter for VMnet8', filter=str,count=6)
pkts = sniff(iface='VMware Virtual Ethernet Adapter for VMnet8', filter=str,count=4,
             prn=lambda x:x[TCP].show())


