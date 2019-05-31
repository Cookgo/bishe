#! -*- coding:utf-8 -*-
from flask import Flask, request, render_template
import json
import re
import complete

app = Flask(__name__)
app.debug = True
ser={}
t=set()
u=set()
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/complete_scan', methods=['POST'])
def proc():
    temp=request.form['port']
    temp=temp.replace(' ','')
    temp = re.split(r',',temp)
    thread_num=request.form['thread_num']
    thread_num=int(thread_num)
    IP=request.form['IP']
    # print(temp)

    scan_port=set()
    for t in temp:
        i=temp.index(t)
        if re.match(r'\w+-\w+',t):
            s=t.split('-')
            start=int(s[0])
            end=int(s[1])
            temp_port=set(range(start,end+1))
            scan_port=scan_port|temp_port
            temp.pop(i)
    temp=list(map(int,temp))
    temp=set(temp)
    scan_port=set(scan_port)
    scan_port=scan_port|set(temp)
    print(scan_port)
    complete.muti_scan(IP,scan_port,thread_num)
    print(complete.result)
    result=json.dumps(complete.result)
    return(result)




@app.route('/ftp_brute',methods=['POST'])
def brute():
    ip=request.form['IP']
    print(ip)
    return ip

# @app.route('/ssh_brute')
# def brute():
#     result=sshp_brute()
#     result = json.dumps(result)
#     return result
#
# @app.route('/syn_flood')
# def brute():
#     result=syn_flood()
#     result = json.dumps(result)
#     return result



if __name__ == '__main__':
    app.run()