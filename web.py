#! -*- coding:utf-8 -*-
from scapy.all import *
import socket
import requests

url="http://192.168.80.130:80/"
try:
    r = requests.get(url)
except:
    print('haven't web)

