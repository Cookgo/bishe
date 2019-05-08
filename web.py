#! -*- coding:utf-8 -*-
from scapy.all import *
import socket
import requests

url="http://192.168.80.130:80/"
r = requests.get(url)
print(r.status_code)
print(r.content)