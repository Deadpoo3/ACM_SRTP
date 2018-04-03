# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcpTest.py'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from socket import *
import os.path
import sys

target = ('192.168.1.108', 1234)


def get_header(name):
    leng = len(name)
    assert leng < 250
    return chr(leng) + name


def send_file(name):
    basename = os.path.basename(name)
    header = bytes(get_header(basename),'utf-8')
    cont = bytes(open(name).read(),'utf-8')
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(target)
    s.sendall(header)
    s.sendall(cont)
    s.close()

send_file("/home/jack/haha")





