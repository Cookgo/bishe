#! -*- coding:utf-8 -*-
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.80.130', 22))
temp=s.recv(1024)
temp=temp.decode()
result=re.(r'\w*ssh\w*',temp)
if result:
    print('hava ssh')
else:
    print('haven't ssh)

