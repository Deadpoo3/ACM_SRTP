# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import socketserver

from PyQt5.QtWidgets import QDialog

import Chat
import dialog
from multiprocessing import Process
import MySQLdb
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ftplib import FTP
import sys, getpass, os.path,ftplib
from PyQt5.QtCore import QFile
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow
import pymysql
from PyQt5.QtWidgets import QMessageBox
import socket


outerip='223.3.91.248'
myip="223.3.91.210"
class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        name_len = ord(self.rfile.read(1))
        name = self.rfile.read(name_len)
        print("Get request:%s" % name)
        path="/home/duyiming/player"
        try:
            os.mkdir(path)
        except:
            print(23)
        name=str(name).strip('b')
        print(name)
        name=name.strip('\'')
        fd = open(path + '/' + name, 'w')
        cont = self.rfile.read(4096)
        while cont:
            fd.write(str(cont))
            cont = self.rfile.read(4096)
        fd.close()
        print("Out :%s" % name)
questionInfo = []

studentInfo=[{'name':'laji',
              'id':123,
              'title':'语文',
              'status':'在达',
              'server':'AC',
              'judge':'tongguo'},
             {'name':'youxiu',
              'id':13,
              'title':'数学',
              'status':'提交',
              'server':'CJ',
              'judge':'拒绝'},
             ]

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 456)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(255, 248, 171);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setStyleSheet("background-image: url(:/image/图片185.png);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setMinimumSize(QtCore.QSize(587, 341))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-image: url(:/image/图片185.png);\n"
"")
        self.widget.setObjectName("widget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-image: url(:/image/纯背景.png);")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        spacerItem1 = QtWidgets.QSpacerItem(37, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 75 10pt \"黑体\";\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_5.addWidget(self.lineEdit_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_5.setStretch(0, 10)
        self.horizontalLayout_5.setStretch(1, 35)
        self.horizontalLayout_5.setStretch(3, 20)
        self.horizontalLayout_5.setStretch(4, 8)
        self.horizontalLayout_5.setStretch(5, 15)
        self.horizontalLayout_5.setStretch(6, 5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-image: url(:/image/纯背景.png);")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_6.addWidget(self.lineEdit_2)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_6.addWidget(self.pushButton_7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("font: 75 10pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_6.addWidget(self.lineEdit_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.horizontalLayout_6.setStretch(0, 10)
        self.horizontalLayout_6.setStretch(1, 35)
        self.horizontalLayout_6.setStretch(3, 20)
        self.horizontalLayout_6.setStretch(4, 8)
        self.horizontalLayout_6.setStretch(5, 15)
        self.horizontalLayout_6.setStretch(6, 5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-image: url(:/image/纯背景.png);")
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_7.addWidget(self.lineEdit_3)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_7.addWidget(self.pushButton_8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("font: 75 10pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_7.addWidget(self.lineEdit_8)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.horizontalLayout_7.setStretch(0, 10)
        self.horizontalLayout_7.setStretch(1, 35)
        self.horizontalLayout_7.setStretch(3, 20)
        self.horizontalLayout_7.setStretch(4, 8)
        self.horizontalLayout_7.setStretch(5, 15)
        self.horizontalLayout_7.setStretch(6, 5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem11 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-image: url(:/image/纯背景.png);")
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_8.addWidget(self.lineEdit_4)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_8.addWidget(self.pushButton_9)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem13)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("font: 75 10pt \"黑体\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_8.addWidget(self.lineEdit_9)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.horizontalLayout_8.setStretch(0, 10)
        self.horizontalLayout_8.setStretch(1, 35)
        self.horizontalLayout_8.setStretch(3, 20)
        self.horizontalLayout_8.setStretch(4, 8)
        self.horizontalLayout_8.setStretch(5, 15)
        self.horizontalLayout_8.setStretch(6, 5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        spacerItem15 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem15)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-image: url(:/image/纯背景.png);")
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_9.addWidget(self.lineEdit_5)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_9.addWidget(self.pushButton_10)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem17)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setStyleSheet("font: 75 10pt \"黑体\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_9.addWidget(self.lineEdit_10)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem18)
        self.horizontalLayout_9.setStretch(0, 10)
        self.horizontalLayout_9.setStretch(1, 35)
        self.horizontalLayout_9.setStretch(3, 20)
        self.horizontalLayout_9.setStretch(4, 8)
        self.horizontalLayout_9.setStretch(5, 15)
        self.horizontalLayout_9.setStretch(6, 5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        spacerItem19 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem19)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem20)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 10pt \"ADMUI3Lg\";\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_10.addWidget(self.pushButton)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem21)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_10.addWidget(self.pushButton_2)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem22)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_10.addWidget(self.pushButton_3)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem23)
        self.horizontalLayout_10.setStretch(0, 35)
        self.horizontalLayout_10.setStretch(1, 5)
        self.horizontalLayout_10.setStretch(2, 20)
        self.horizontalLayout_10.setStretch(3, 5)
        self.horizontalLayout_10.setStretch(4, 150)
        self.horizontalLayout_10.setStretch(5, 10)
        self.horizontalLayout_10.setStretch(6, 30)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.widget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")




        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem24 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem24)
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_4.addWidget(self.pushButton_13)
        spacerItem25 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem25)
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_4.addWidget(self.pushButton_16)
        spacerItem26 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem26)
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_4.addWidget(self.pushButton_14)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem27)
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_4.addWidget(self.pushButton_17)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem28)
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_4.addWidget(self.pushButton_15)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 5)
        self.verticalLayout_4.setStretch(2, 2)
        self.verticalLayout_4.setStretch(3, 2)
        self.verticalLayout_4.setStretch(4, 2)
        self.verticalLayout_4.setStretch(5, 5)
        self.verticalLayout_4.setStretch(6, 2)
        self.verticalLayout_4.setStretch(7, 5)
        self.verticalLayout_4.setStretch(8, 10)
        self.verticalLayout_4.setStretch(9, 5)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem29 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem29)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_12.addWidget(self.lineEdit_11)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem30)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_12.addWidget(self.pushButton_11)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem31)
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_12.addWidget(self.pushButton_12)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem32)
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_12.addWidget(self.pushButton_18)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem33)
        self.horizontalLayout_12.setStretch(0, 2)
        self.horizontalLayout_12.setStretch(1, 5)
        self.horizontalLayout_12.setStretch(2, 10)
        self.horizontalLayout_12.setStretch(3, 5)
        self.horizontalLayout_12.setStretch(4, 5)
        self.horizontalLayout_12.setStretch(5, 5)
        self.horizontalLayout_12.setStretch(6, 5)
        self.horizontalLayout_12.setStretch(9, 12)
        self.gridLayout.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_2, "")








        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setStyleSheet("color: rgb(63, 0, 0);\n"
"font: 75 12pt \"黑体\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8, 0, QtCore.Qt.AlignRight)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setStyleSheet("color: rgb(63, 0, 0);\n"
"font: 75 12pt \"黑体\";")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9, 0, QtCore.Qt.AlignLeft)
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_2.addWidget(self.label_25)
        self.horizontalLayout_2.setStretch(0, 7)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setStyleSheet("border-image: url(:/image/纯背景.png);")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        spacerItem34 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem34)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem35 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem35)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"黑体\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem36)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"黑体\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem37)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 15)
        self.horizontalLayout_3.setStretch(3, 2)
        self.horizontalLayout_3.setStretch(4, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 672, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        self.events()
        self.addnewoneevent()
        self.setTableView()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "添加文件"))
        self.label.setText(_translate("MainWindow", "     题目名称："))
        self.pushButton_7.setText(_translate("MainWindow", "添加文件"))
        self.label_2.setText(_translate("MainWindow", "         输入："))
        self.pushButton_8.setText(_translate("MainWindow", "添加文件"))
        self.label_3.setText(_translate("MainWindow", "         输出："))
        self.pushButton_9.setText(_translate("MainWindow", "添加文件"))
        self.label_4.setText(_translate("MainWindow", "         答案："))
        self.pushButton_10.setText(_translate("MainWindow", "添加文件"))
        self.label_5.setText(_translate("MainWindow", "   测试点个数："))
        self.pushButton.setText(_translate("MainWindow", "添加新题目"))
        self.pushButton_2.setText(_translate("MainWindow", "保存"))
        self.pushButton_3.setText(_translate("MainWindow", "确认提交"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "发题"))
        self.pushButton_13.setText(_translate("MainWindow", "刷新"))
        self.pushButton_16.setText(_translate("MainWindow", "下载选手答案"))
        self.pushButton_14.setText(_translate("MainWindow", "去评测"))
        self.pushButton_17.setText(_translate("MainWindow", "id升序排列"))
        self.pushButton_15.setText(_translate("MainWindow", "提交"))
        self.label_11.setText(_translate("MainWindow", "姓名："))
        self.pushButton_11.setText(_translate("MainWindow", "查询"))
        self.pushButton_12.setText(_translate("MainWindow", "聊天"))
        self.pushButton_18.setText(_translate("MainWindow", "连接"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "状态"))
        self.label_8.setText(_translate("MainWindow", "学生姓名："))
        self.label_9.setText(_translate("MainWindow", "  题目名称："))
        self.pushButton_4.setText(_translate("MainWindow", " 通过"))
        self.pushButton_5.setText(_translate("MainWindow", "拒绝"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "评测"))

    def buttonclicked6(self):
        file_name=self.showDialog()
        self.lineEdit_2.setText(str(file_name[0]))
    def buttonclicked7(self):
        file_name=self.showDialog()
        self.lineEdit_3.setText(str(file_name[0]))
    def buttonclicked8(self):
        file_name=self.showDialog()
        self.lineEdit_4.setText(str(file_name[0]))
    def buttonclicked9(self):
        file_name=self.showDialog()
        self.lineEdit_5.setText(str(file_name[0]))
    def buttonclicked5(self):
        file_name = self.showDialog()
        self.lineEdit.setText(str(file_name[0]))
    def events(self):
        self.pushButton_8.clicked.connect(self.buttonclicked7)
        self.pushButton_6.clicked.connect(self.buttonclicked5)
        self.pushButton_7.clicked.connect(self.buttonclicked6)
        self.pushButton_9.clicked.connect(self.buttonclicked8)
        self.pushButton_10.clicked.connect(self.buttonclicked9)
        #self.pushButton.clicked.connect(self.lineEdit_10.clear)
    def showDialog(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        return filename
    def addnewoneevent(self):
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        self.pushButton.clicked.connect(self.lineEdit_3.clear)
        self.pushButton.clicked.connect(self.lineEdit_4.clear)
        self.pushButton.clicked.connect(self.lineEdit_5.clear)
        self.pushButton.clicked.connect(self.lineEdit_6.clear)
        self.pushButton.clicked.connect(self.lineEdit_7.clear)
        self.pushButton.clicked.connect(self.lineEdit_8.clear)
        self.pushButton.clicked.connect(self.lineEdit_9.clear)
        self.pushButton.clicked.connect(self.lineEdit_10.clear)
        self.pushButton_2.clicked.connect(self.safe)
        self.pushButton_3.clicked.connect(self.commitQues)
        self.pushButton_4.clicked.connect(self.passQuestion)
        self.pushButton_5.clicked.connect(self.rejQuestion)
        self.pushButton_17.clicked.connect(self.sortbyid)
        self.pushButton_18.clicked.connect(self.connectserver)
        self.pushButton_13.clicked.connect(self.updateStuAns)
        self.pushButton_14.clicked.connect(self.judgeThisone)
        self.pushButton_16.clicked.connect(self.downloadThisone)
        self.pushButton_12.clicked.connect(self.chat)
        self.pushButton_15.clicked.connect(self.upload)
    def upload(self):
            conn = MySQLdb.connect(
                    host=outerip,
                    port=3306,
                    user='root',
                    password='root',
                    db='python',
                    charset='utf8'
            )
            cur = conn.cursor()
            sqlsequnce = 'update submit set refereeCheck=%s where name =%s'
            rows = self.model.rowCount()
            print(rows)
            for rows_index in range(rows):
                    if self.model.item(rows_index, 5) is None:
                            continue
                    if self.model.item(rows_index, 5).text()=='Pass':
                        print()
                        cur.execute(sqlsequnce,('Pass',self.model.item(rows_index, 0).text()))
            cur.close()
            conn.commit()
            conn.close()
            print('success')
    def chat(self):
            win = Chat.Ui_Chat('duyiming', ip=outerip, port=3378)
            win.createThread()
            win.show()
            win.exec_()

            #sys.exit(app.exec_())
    def safe(self):
        qurl=[]
        qurl.append(self.lineEdit.text())
        qurl.append(self.lineEdit_2.text())
        qurl.append(self.lineEdit_3.text())
        qurl.append(self.lineEdit_4.text())
        qurl.append(self.lineEdit_5.text())
        questionone={ 'qurl':qurl,
                      'title':self.lineEdit_6.text(),
                      'input':self.lineEdit_7.text(),
                      'output':self.lineEdit_8.text(),
                      'answer':self.lineEdit_9.text(),
                      'testNum':self.lineEdit_10.text()
                      }
        questionInfo.append(questionone)
    def updateStuAns(self):
            conn = MySQLdb.connect(
                    host=outerip,
                    port=3306,
                    user='root',
                    password='root',
                    db='python',
                    charset='utf8'
            )
            cur = conn.cursor()
            sqlsequnce='SELECT * FROM submit'
            cur.execute(sqlsequnce)
            data=cur.fetchall()
            i=0
            print(2222222222222222222)
            for one in data:                                                  #刷新数据
                self.model.setItem(i, 0, QtGui.QStandardItem(_fromUtf8(one[1])))
                self.model.setItem(i,1,QtGui.QStandardItem(_fromUtf8(str(one[0]))))
                self.model.setItem(i, 2, QtGui.QStandardItem(_fromUtf8(one[2])))
                self.model.setItem(i, 3, QtGui.QStandardItem(_fromUtf8(one[4])))
                self.model.setItem(i, 4, QtGui.QStandardItem(_fromUtf8(one[3])))
                self.model.setItem(i, 5, QtGui.QStandardItem(_fromUtf8(one[5])))
                i=i+1
                print(one)
            #sqlseq = 'INSERT INTO submit(id,name,question,result,isSubmit,refereeCheck) values(%s,%s,%s,%s,%s,%s)'
            #cur.execute(sqlseq,('2','sdf','shuxsadue','accept','k','pass'))
            conn.commit()
           # result=cur.fetchall()
           # print(result)
            print('success')
    def commitQues(self):
        conn=MySQLdb.connect(
                    host=outerip,
                    port=3306,
                    user='root',
                    password='root',
                    db='python',
                    charset = 'utf8'
                )
        cur= conn.cursor()
        qurl=self.lineEdit.text()+self.lineEdit_2.text()+self.lineEdit_3.text()+self.lineEdit_4.text()+self.lineEdit_5.text()
        sqlseq='INSERT INTO question(url,title,input,output,point) values(%s,%s,%s,%s,%s)'
        cur.execute(sqlseq,(qurl,self.lineEdit_6.text(),self.lineEdit_7.text(),self.lineEdit_8.text(),
                            self.lineEdit_10.text()))
        print('success')
        # my=cur.execute('select * from user')
        # values=my.fetchall()
        # print(values)
        #print(sqld)
        cur.close()
        conn.commit()#关闭cursor对象
        conn.close()
    def showstatus(self,name,question):    #展示题目状态

        self.label_10.setText(name)
        self.label_25.setText(question)
        filepath='/home/duyiming/player'
        input = open(filepath+'/'+'haha', 'r')
        self.textEdit.append(str(input.read()))
    def passQuestion(self):
        reply=self.closeEvent()
        if reply ==QMessageBox.Yes:
            self.tabWidget.setCurrentIndex(1)
            rows = self.model.rowCount()
            for rows_index in range(rows):
                    # print items[item_index].text()
                    if self.model.item(rows_index, 0) is None:
                            continue
                    if self.model.item(rows_index, 0).text()==self.label_10.text():
                        self.model.setItem(rows_index, 5, QtGui.QStandardItem(_fromUtf8('Pass')))
                    #print(self.model.item(rows_index, 0).text())
            print(self.label_10.text())
            self.label_10.setText('')
            self.label_25.setText('')
            self.textEdit.setText('')
    def rejQuestion(self):
        reply=self.closeEvent()
        if reply ==QMessageBox.Yes:
            self.tabWidget.setCurrentIndex(1)
            self.label_10.setText('')
            self.label_25.setText('')
            self.textEdit.setText('')
    def closeEvent(self):
        reply = QMessageBox.question(self.tab_3,
                                     'Message',
                                     'You sure to commit?',
                                     QMessageBox.Yes | QMessageBox.No)
        return reply
    def setTableView(self):
            self.model = QtGui.QStandardItemModel(self.tableView)

            # 设置表格属性：
            self.model.setRowCount(17)
            self.model.setColumnCount(6)

            # 设置表头
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, _fromUtf8(u"学生姓名"))
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, _fromUtf8(u"学生id"))
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, _fromUtf8(u"题目"))
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, _fromUtf8(u"答题状态"))
            self.model.setHeaderData(4, QtCore.Qt.Horizontal, _fromUtf8(u"服务器评测结果"))
            self.model.setHeaderData(5, QtCore.Qt.Horizontal, _fromUtf8(u"裁判审核"))

            self.tableView.setModel(self.model)
            self.tableView.setColumnWidth(0, 80)
            self.tableView.setColumnWidth(1, 80)
            self.tableView.setColumnWidth(2, 80)
            self.tableView.setColumnWidth(3, 80)
            self.tableView.setColumnWidth(4, 200)
            self.tableView.setColumnWidth(5, 80)
            # self.model.setItem(2, 2, QtGui.QStandardItem(_fromUtf8('45')))
            # self.model.setItem(3, 2, QtGui.QStandardItem(_fromUtf8('8')))
            self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    def sortbyid(self):
         self.tableView.sortByColumn(1, QtCore.Qt.AscendingOrder)
    def queryStudentStatus(self):
         querycondition=self.lineEdit_11.text()
         for studentone in studentInfo:
             if studentone['name'].find(querycondition):
                     self.model.appendRow([
                     QStandardItem("row %s, column %s"%(11,11)),
                     QStandardItem("row %s, column %s"%(11,11)),
                     QStandardItem("row %s, column %s"%(11,11)),
                     QStandardItem("row %s, column %s"%(11,11)),
    ])
    def connectserver(self):
            addr = (myip, 1234)

            server = socketserver.TCPServer(addr, MyTCPHandler)
            server.serve_forever()
    def downloadThisone(self):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((outerip, 3244))
            print(s.recv(1024))
            row = self.tableView.currentIndex().row()
            row=1
            name = self.model.item(row,0).text()
            print(name)
            name='3;'+name
            print(name)
            try:
                s.send(bytes(name, encoding='utf8'))
            except:
                print(s.recv(1024))
            #s.send(bytes('exit', encoding='utf8'))
            s.close()
    def judgeThisone(self):
        row = self.tableView.currentIndex().row()
        name=self.model.item(row,0).text()
        question=self.model.item(row,2).text()
        self.tabWidget.setCurrentIndex(2)
        self.showstatus(name,question)

if __name__=='__main__':

    app=QApplication(sys.argv)
    # d=QDialog()
    # we=dialog.Ui_Dialog()
    # we.setupUi(d)

    nn=QMainWindow()
    w=Ui_MainWindow()
    w.setupUi(nn)
    #we.exec_()

    sys.exit(app.exec_())
