#! -*- coding:utf-8 -*-
from flask import Flask, request, render_template
import nmap
import json
app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/A_scan', methods=['POST'])
def proc():
    IP=request.form['IP']
    print(IP)
    nm = nmap.PortScanner()
    nm.scan(IP, '1-30 ')
    tcpport = nm[IP].all_tcp()
    udpport = nm[IP].all_udp()
    port=set()
    protocol = {}
    service={}
    solfware={}
    version={}

    for tcp in tcpport:
        if nm[IP]['tcp'][tcp]['state'] == 'open':
            port.add(tcp)
            protocol[tcp]='tcp'
            service[tcp]=nm[IP]['tcp'][tcp]['name']
            solfware[tcp]=nm[IP]['tcp'][tcp]['product']
            version[tcp]=nm[IP]['tcp'][tcp]['version']
    for udp in udpport:
        if nm[IP]['udp'][udp]['state'] == 'open':
            port.add(udp)
            protocol[udp] = 'udp'
            service[udp] = nm[IP]['udp'][udp]['name']
            solfware[udp]= nm[IP]['udp'][udp]['product']
            version[udp]= nm[IP]['udp'][udp]['version']
    # print(port)
    # print(service)
    # print(solfware)
    # print(version)
    result={}
    for p in port:
        result[p]=protocol[p]+'-'+service[p]+'-'+solfware[p]+'-'+version[p]
    print(result)
    result = json.dumps(result)
    return result





if __name__ == '__main__':
    app.run()