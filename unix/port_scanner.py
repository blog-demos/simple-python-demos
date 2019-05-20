# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   端口扫描程序

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/8
Last Modify: 2016/3/9
version: 0.0.1
'''

import optparse
import socket

def conn_scan(tgt_host, tgt_port):
    try:
        conn_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_skt.connect((tgt_host, tgt_port))
        conn_skt.send("ViolentPython\r\n")
        result = conn_skt.recv(100)
        print('[+]{0}/tcp open'.format(tgt_port))
        print("[+] {0}".format(result))
        conn_skt.close()
    except Exception, e:
        print("[-]{0}/tcp closed\n{1}".format(tgt_port, e))

def port_scan(tgt_host, tgt_ports):
    try:
        tgt_ip = socket.gethostbyname(tgt_host)
    except Exception, e:
        print("[-] Cannot resolve '{0}': Unknown host{1}".format(tgt_host, e))
        return
    try:
        tgt_name = socket.gethostbyaddr(tgt_ip)
        print('\n[+] Scan Results for: {0}'.format(tgt_name[0]))
    except Exception, e:
        print("\n[+] Scan Results for: {0}\n{1}".format(tgt_host, e))
    socket.setdefaulttimeout(1)
    for tgtPort in tgt_ports:
        print('\nScanning port ' + str(tgtPort))
        conn_scan(tgt_host, int(tgtPort))

# 测试是否有效
# port_scan('www.baidu.com', [80, 443, 3389, 1433, 23, 445])

def scanning():
    parser = optparse.OptionParser('usage %prog –H <targethost> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='int', help='specify target port')
    (options, args) = parser.parse_args()
    tgt_host = options.tgtHost
    tgt_port = options.tgtPort
    args.append(tgt_port)
    if tgt_host is None or tgt_port is None:
        print("print('[-] You must specify a target host and port[s]!")
        exit(0)

    port_scan(tgt_host, args)

if __name__ == '__main__':
    scanning()
