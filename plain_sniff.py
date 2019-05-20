#! -*- coding:utf-8 -*-
from scapy.all import *
def callback(pkt):
    if pkt.haslayer(TCP):
        if pkt[TCP].payload:
            data=pkt[TCP].payload

            data=str(data)
            print(type(data))
            print(data)




# pkt=IP(dst='192.168.0.1')/TCP()/'dsafsadsa'
# data=pkt.load.decode('utf-8')
# print(data)
dpkt=sniff(filter='tcp port 80 and ip 192.168.80.130',prn=callback,count=10)
# scapy.wrpcap("demo.pcap", dpkt)
# pkts = scapy.rdpcap(r'C:\Users\dkl\Desktop\bishe\demo.pcap')
# i=1
# for pkt in pkts:
#     pkt.show()
#     i=i+1
#     if i>3:
#         break
# pkts[3].show()