#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
import nmap

result = {}
lock = threading.Lock()


def scan(IP, p):

    global result
    global lock
    p = str(p)
    p = p[1:-1]
    nm = nmap.PortScanner()
    nm.scan(IP, p)
    # print(id(nm))
    tcpport = nm[IP].all_tcp()
    print(tcpport)
    udpport = nm[IP].all_udp()
    port = set()
    protocol = {}
    service = {}
    solfware = {}
    version = {}

    for tcp in tcpport:

        if nm[IP]['tcp'][tcp]['state'] == 'open':
            port.add(tcp)
            protocol[tcp] = 'tcp'
            service[tcp] = nm[IP]['tcp'][tcp]['name']
            solfware[tcp] = nm[IP]['tcp'][tcp]['product']
            version[tcp] = nm[IP]['tcp'][tcp]['version']
    for udp in udpport:
        if nm[IP]['udp'][udp]['state'] == 'open':
            port.add(udp)
            protocol[udp] = 'udp'
            service[udp] = nm[IP]['udp'][udp]['name']
            solfware[udp] = nm[IP]['udp'][udp]['product']
            version[udp] = nm[IP]['udp'][udp]['version']
    for p in port:
        lock.acquire()
        result[p] = protocol[p] + '-' + service[p] + '-' + solfware[p] + '-' + version[p]
        lock.release()


def muti_scan(IP, p, thread_num):
    name = []

    if thread_num > 0:
        times = int(len(p) / thread_num)
        if times>20:
            p = list(p)
            for i in range(thread_num):
                t = threading.Thread(target=scan, args=(IP, p[i * times:(i + 1) * times]))
                t.start()
                name.append(t)
                # print(t)
            for i in range(thread_num):
                name[i].join()
            if p[thread_num * times:]:
                scan(IP, p[thread_num * times:])
        else:
            scan(IP, p)

    else:
        scan(IP, p)






# print(result)

if __name__ == '__main__':
    scan('192.168.80.130',[0])
    print(result)

