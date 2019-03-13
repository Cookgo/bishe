#!/usr/bin/python
# -*- coding:utf-8 -*-
import nmap
nm=nmap.PortScanner()
nm.scan('127.0.0.1', '1-1000')
nm.scaninfo()
nm.all_hosts()