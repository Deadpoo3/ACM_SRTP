# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, threading, time, socket
import sourceChat


class Ui_Chat(QtWidgets.QMainWindow):
    def __init__(self, name, ip, port):
        super(Ui_Chat, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.uname = name
        self.threads = []
        self.Ip = ip
        self.Port = port
        self.BUFSIZ = 1024
        self.tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpCliSock.connect((self.Ip,self.Port))
        self.recvThread = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        MainWindow.setStyleSheet("background-color: rgb(233, 255, 255);")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralWidget)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_minus = QtWidgets.QPushButton(self.centralWidget)
        self.btn_minus.setStyleSheet("border-radius:17px;padding:1px 1px")
        self.btn_minus.clicked.connect(self.showMinimized)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minus.setIcon(icon)
        self.btn_minus.setIconSize(QtCore.QSize(30, 30))
        self.btn_minus.setObjectName("btn_minus")
        self.horizontalLayout.addWidget(self.btn_minus)
        self.btn_close = QtWidgets.QPushButton(self.centralWidget)
        self.btn_close.setStyleSheet("border-radius:17px;padding:1px 1px")
        self.btn_close.clicked.connect(self.resetClose)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/prefix1/close21.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QtCore.QSize(37, 37))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_Edit = QtWidgets.QTextEdit(self.centralWidget)
        self.txt_Edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_Edit.setObjectName("txt_Edit")
        self.verticalLayout_2.addWidget(self.txt_Edit)
        self.txt_msg = QtWidgets.QTextEdit(self.centralWidget)
        self.txt_msg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_msg.setObjectName("txt_msg")
        self.verticalLayout_2.addWidget(self.txt_msg)
        self.verticalLayout_2.setStretch(0, 20)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_namlist = QtWidgets.QComboBox(self.centralWidget)
        self.cb_namlist.setObjectName("cb_namlist")
        self.cb_namlist.addItem('aaaa')
        self.cb_namlist.addItem('duyiming')
        self.verticalLayout.addWidget(self.cb_namlist)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_send = QtWidgets.QPushButton(self.centralWidget)
        self.btn_send.setStyleSheet("border:2px groove gray;")
        self.btn_send.setObjectName("btn_send")
        self.btn_send.clicked.connect(self.sendMess)
        self.verticalLayout.addWidget(self.btn_send)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_send.setText(_translate("MainWindow", "PushButton"))

    def resetClose(self):
        self.tcpCliSock.close()
        return self.close()

    # def choseImg(self):
    #     imgPath = QtWidgets.QFileDialog.getOpenFileName()
    #     self.img = imgPath[0]
    #     if self.img:
    #         self.txt_msg.insertPlainText('<img src=' + "'" + self.img + "'>")

    def sendMess(self):
        self.tcpCliSock.send(bytes('to:' + self.cb_namlist.currentText(), 'UTF-8'))
        messg = self.txt_msg.toPlainText()
        if messg:
            if messg == 'quit':
                self.tcpCliSock.close()
            else:
                self.tcpCliSock.send(messg.encode(encoding='UTF-8'))
                self.txt_Edit.append('\n-------------[%s]' %(time.ctime()) + ' ' + self.uname + ':\n')
                self.txt_Edit.append(messg)
                self.txt_Edit.append('\n')

    def Recv(self, sock, test):
        while True:
            recData = sock.recv(self.BUFSIZ).decode()
            print(recData)
            if recData:
                if recData == 'quit':
                    sock.close()
                    break
                elif recData == 'judge':
                    self.cb_namlist.addItems(recData[1::])
                else:
                    self.txt_Edit.append(recData)
                    self.txt_Edit.append('\n')

    def createThread(self):
        self.tcpCliSock.send(bytes(';' + self.uname,'utf-8'))
        self.recvThread = threading.Thread(target=self.Recv, args=(self.tcpCliSock, None))
        self.recvThread.start()

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#
#     win = Ui_Chat(None, None, None)
#     win.show()
#
#     sys.exit(app.exec_())
