#! -*- coding:utf-8 -*-
from scapy.all import *
import paramiko
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('192.168.80.130',port=22,username='root',password='12345678')
# print('chenggong')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.80.130',22,'root', '12345678')
print('chenggong')