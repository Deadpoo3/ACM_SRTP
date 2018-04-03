#encoding=utf-8
#创建一个socketseverTCP服务器
import string
import time
import socket
import threading
import login
import FTransfer
import pymysql,re
import assign


def tcplink(sock,addr):
    print ('Accept new connection from %s:%s...'% addr)
    sock.send(bytes('Welcome!','utf-8'))
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if data=='exit' or not data:
            break
        Data=data.decode()
        mess=Data.split(';')
        flag=mess[0]
        if flag=='0':
            Uname=mess[1]
            id=mess[1]
            password=mess[2]
            res=login.Ulogin(id,password)
            conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='root',
                db='python',
            )
            cur = conn.cursor()
            cur.execute("select Q.url from user U,question Q where U.name=%s", [Uname])
            aa = str(cur.fetchall())
            aa = re.findall('\'(.+?)\'', aa)
            ss = ""
            for i in range(0, len(aa)):
                ss += aa[i]
                ss += ";"
            print(ss)
            sock.send(bytes(res+ss, 'utf-8'))
            #检查用户名密码是否正确
        elif flag=='1':
            id = mess[1]
            password = mess[2]
            assign.register(id,password)
        elif flag=='3':
            Uname=mess[1]
            conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='root',
                db='python',
            )
            cur = conn.cursor()
            print(Uname)
            cur.execute("select S.url from submit S where S.name=%s", [Uname])
            aa = str(cur.fetchall())
            aa = re.findall('\'(.+?)\'', aa)
            ss = ""
            for i in range(0, len(aa)):
                ss += aa[i]
            print(ss)
            FTransfer.send_file(ss);
    print ('Connection from %s:%s closed.'%addr)


host='223.3.91.248'
port=3244
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
print ('Waiting for connection...')
while 1:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink(sock,addr))