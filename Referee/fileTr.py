#!/usr/bin/python3
# -*- coding:utf-8 -*-
from ftplib import FTP
import sys, getpass, os.path,ftplib

def transfer(fileName,ID):
    f = FTP()
    f.connect('192.168.1.106',21)
    f.login('player1', '123456')

    file = os.path.basename(fileName)
    (shotname,extension) = os.path.splitext(file)
    print(shotname)
    filename = '/player1/' + ID   
    try:
        f.mkd(filename)
    except ftplib.error_perm:
        f.cwd(filename)
    else:
        f.cwd(filename)

    localfile = fileName
    fd=open(localfile,'rb')

    f.storbinary('STOR %s' % os.path.basename(localfile),fd)
    fd.close()
    f.close()

    return 1

