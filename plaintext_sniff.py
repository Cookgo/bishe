#! -*- coding:utf-8 -*-
from scapy.all import *
def callback(pkt):
    if pkt.haslayer(TCP):
        if pkt[TCP].payload:
            data=pkt[TCP].payload
            # pkt.show()
            # pkt.show()
            # print(type(data))
            data=str(data)
            # print(type(data))
            str1=data[2:-1]
            str1 =eval("u"+"\""+str1+"\"")
            str1.decode('utf-8')
            print(type(str1))
            print(str1)
            # print(str1.decode('unicode'))



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