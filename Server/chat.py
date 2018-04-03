

from socket import *
from time import ctime
import threading
import re

HOST = '223.3.91.248'
PORT = 3378
BUFSIZ = 1024
ADDR = (HOST, PORT)


def Deal(sock, user):
    while True:
        data = sock.recv(BUFSIZ).decode()
        print(data)
        if data == 'quit':
            del clients[user]
            sock.send(data)
            sock.close()
            print('%s logout' % user)
            break
        elif re.match('to:.+', data) is not None:
            data = data[3:]
            if data in clients:
                chatwith[sock] = clients[data]
                chatwith[clients[data]] = sock
            else:
                sock.send(bytes('the user %s is not exist' % data,'utf-8'))
        else:
            if sock in chatwith:
                chatwith[sock].send(bytes("[%s] %s:\n %s" % (ctime(), user, data),'utf-8'))
                print("[%s] %s:\n %s" % (ctime(), user, data))
            #else:
                #sock.send('Please input the user who you want to chat with')


tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

clients = {}
chatwith = {}

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)
    username = tcpCliSock.recv(BUFSIZ)
    print (username)
    uname = username.decode().split(";")
    print('The username is:', uname[1])

    clients[uname[1]] = tcpCliSock
    chat = threading.Thread(target=Deal, args=(tcpCliSock, uname[1]))
    chat.start()

tcpSerSock.close()