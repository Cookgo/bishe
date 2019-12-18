#! -*- coding:utf-8 -*-
from flask import Flask, request, render_template
import json
import re
import sys
import complete
import ftp_force
import ssh_force
import nmap
import dos

app = Flask(__name__)
app.debug = True
ser = {}
t = set()
u = set()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/scan', methods=['POST'])
def proc():
    complete.result={}
    temp = request.form['port']
    temp = temp.replace(' ', '')
    temp = re.split(r',', temp)
    thread_num = request.form['thread_num']
    thread_num = int(thread_num)
    IP = request.form['IP']
    # print(temp)

    scan_port = set()
    for t in temp:
        i = temp.index(t)
        if re.match(r'\w+-\w+', t):
            s = t.split('-')
            start = int(s[0])
            end = int(s[1])
            temp_port = set(range(start, end + 1))
            scan_port = scan_port | temp_port
            temp.pop(i)
    temp = list(map(int, temp))
    temp = set(temp)
    scan_port = set(scan_port)
    scan_port = scan_port | set(temp)
    print(scan_port)
    complete.muti_scan(IP, scan_port, thread_num)
    print(complete.result)
    result = json.dumps(complete.result)
    return (result)


@app.route('/ftp_brute', methods=['POST'])
def f_brute():
    IP = request.form['IP']
    port = int(request.form['port'])
    thread_num = int(request.form['thread_num'])
    print(IP)
    print(port)
    print(thread_num)

    nm = nmap.PortScanner()
    p = str(port)
    nm.scan(IP, p)
    if (nm[IP]['tcp'][port]['name'] != 'ftp')or (nm[IP]['tcp'][port]['state']!='open'):

        print(nm[IP]['tcp'][port]['name'])
        return '该端口没有ftp服务'

    ftp_force.brute(thread_num, IP, port)
    print(ftp_force.result)
    ftp_force.result['tip0'] = 'FTP服务爆破测试结果：\n  主机：' + IP + ',' + '端口: ' + str(port) + '。\n'
    if ftp_force.result['count'] > 100:
        ftp_force.result['tip2'] = '  共尝试登录：' + str(
            ftp_force.result['count']) + '次，尝试次数超过100次，存在可爆破风险，建议增加一定限制措施，比如同一ip不能在短时间尝试过多次数等。\n'
    else:
        ftp_force.result['tip2'] = '  共尝试登录：' + str(ftp_force.result['count']) + '次，尝试次数无法超过100次，没有遭受爆破攻击风险。'
    if 'username' in ftp_force.result:
        ftp_force.result['tip1'] = '  破解成功,' + '用户名：' + str(ftp_force.result['username']) + ' 密码：' + str(
            ftp_force.result['password']) + ',存在若口令缺陷，建议使用强密码，即数字、字母以及特殊符号混合的密码。\n'
    else:
        ftp_force.result['tip1'] = '  破解失败，密码复杂，爆破难度较高。\n'
    result = ftp_force.result['tip0'] + ftp_force.result['tip1'] + ftp_force.result['tip2']
    print(result)
    # result=json.dumps(result)
    return result


@app.route('/ssh_brute', methods=['POST'])
def s_brute():
    IP = request.form['IP']
    port = int(request.form['port'])
    thread_num = int(request.form['thread_num'])
    print(IP)
    print(port)
    print(thread_num)

    nm = nmap.PortScanner()
    p = str(port)
    nm.scan(IP, p)
    if nm[IP]['tcp'][port]['name'] != 'ssh' or nm[IP]['tcp'][port]['state']!='open':
        return '该端口没有ssh服务'

    ssh_force.brute(thread_num, IP, port)
    ssh_force.result['tip0'] = 'SSH服务爆破测试结果：\n  主机:' + IP + ',' + '端口: ' + str(port) + '。\n'
    if ssh_force.result['count'] > 100:
        ssh_force.result['tip2'] = '  共尝试登录：' + str(
            ssh_force.result['count']) + '次，尝试次数超过100次，存在可爆破风险，建议增加一定限制措施，比如同一ip不能在短时间尝试过多次数等。\n'
    else:
        ssh_force.result['tip2'] = '  共尝试登录：' + str(ssh_force.result['count']) + '次，尝试次数无法超过100次，没有遭受爆破攻击风险。'
    if 'username' in ssh_force.result:
        ssh_force.result['tip1'] = '  破解成功,' + '用户名：' + str(ssh_force.result['username']) + ' 密码：' + str(
            ssh_force.result['password']) + ',存在若口令缺陷，建议使用强密码，即数字、字母以及特殊符号混合的密码。\n'
    else:
        ssh_force.result['tip1'] = '  破解失败，密码复杂，爆破难度较高。\n'
    result = ssh_force.result['tip0'] + ssh_force.result['tip1'] + ssh_force.result['tip2']
    print(result)
    return result


@app.route('/dos_test', methods=['POST'])
def dos_test():
    IP = request.form['IP']
    print(IP)
    port = int(request.form['port'])
    print(port)
    dos.syn_test(IP, port)
    if dos.flag:
        return 'DOS测试结果\n  经测试，发送一个syn包，收到超过4个syn ack包，存在syn泛洪攻击的可能。'
    else:
        return 'DOS测试结果\n  经测试，发送一个syn包，收到不超过4个syn ack包，遭到syn泛洪攻击的可能较小。'


if __name__ == '__main__':
    # app.config['JSON_AS_ASCII'] = False
    app.run()
