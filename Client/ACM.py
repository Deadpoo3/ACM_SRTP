# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ACM.py'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from ftplib import FTP
import sys, os, ftplib, time
import IP, SignUp, client, Chat, sourceACM, myButton
import pymysql, socket, threading


class Ui_ACM(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_ACM, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.IP = ''
        self.judge = ''
        self.pwd = ''
        self.recv = None
        self.conn = None
        self.sock = None
        self.port1 = 1234
        self.port2 = 3244
        self.port3 = 3378

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

        self.counter = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1066, 625)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # central widget
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setStyleSheet("background-color: rgb(233, 255, 255);")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # left widget
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setStyleSheet("background-color: rgb(103, 210, 255);")
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # 设置服务器IP
        self.btn_server = QtWidgets.QPushButton(self.widget)
        self.btn_server.setStyleSheet("border:2px groove gray;")
        self.btn_server.setObjectName("btn_server")
        self.btn_server.clicked.connect(self.showIPWin)
        self.verticalLayout_2.addWidget(self.btn_server)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # 注册窗口
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_Id = QtWidgets.QLabel(self.widget)
        self.lbl_Id.setStyleSheet("")
        self.lbl_Id.setObjectName("lbl_Id")
        self.gridLayout.addWidget(self.lbl_Id, 2, 0, 1, 1)
        self.lbl_pwd = QtWidgets.QLabel(self.widget)
        self.lbl_pwd.setObjectName("lbl_pwd")
        self.gridLayout.addWidget(self.lbl_pwd, 3, 0, 1, 1)
        self.led_pwd = QtWidgets.QLineEdit(self.widget)
        self.led_pwd.setStyleSheet(
            "background-image: url(:/new/prefix1/d439b6003af33a87c0ba0445c55c10385243b59d.jpg);\n"
            "border:2px groove gray;border-radius:10px;padding:2px 4px")
        self.led_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.led_pwd.setObjectName("led_pwd")
        self.gridLayout.addWidget(self.led_pwd, 3, 1, 1, 1)
        self.led_Id = QtWidgets.QLineEdit(self.widget)
        self.led_Id.setStyleSheet("background-image: url(:/new/prefix1/d439b6003af33a87c0ba0445c55c10385243b59d.jpg);\n"
                                  "border:2px groove gray;border-radius:10px;padding:2px 4px")
        self.led_Id.setObjectName("led_Id")
        self.gridLayout.addWidget(self.led_Id, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_login = QtWidgets.QPushButton(self.widget)
        self.btn_login.setStyleSheet("border:2px groove gray;")
        self.btn_login.setObjectName("btn_login")
        self.btn_login.clicked.connect(self.login)
        self.horizontalLayout_2.addWidget(self.btn_login)
        self.btn_signUp = QtWidgets.QPushButton(self.widget)
        self.btn_signUp.setStyleSheet("border:2px groove gray;")
        self.btn_signUp.setObjectName("btn_signUP")
        self.btn_signUp.clicked.connect(self.signUp)
        self.horizontalLayout_2.addWidget(self.btn_signUp)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        # 任务列表
        self.listOfTask = QtWidgets.QComboBox(self.widget)
        self.listOfTask.setStyleSheet("")
        self.listOfTask.setObjectName("listOfTask")
        self.listOfTask.insertItem(0,'   ')

        self.verticalLayout_2.addWidget(self.listOfTask)

        self.btn_getTask = QtWidgets.QPushButton(self.widget)
        self.btn_getTask.setStyleSheet("border:2px groove gray;")
        self.btn_getTask.setObjectName("btn_getTask")
        self.btn_getTask.setText("getTask")
        #self.btn_getTask.clicked.connect(self.getTask)
        self.btn_getTask.setEnabled(False)
        self.verticalLayout_2.addWidget(self.btn_getTask)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addWidget(self.widget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)

        # 最大化最小化正常化
        self.btn_minus = QtWidgets.QPushButton(self.centralWidget)
        self.btn_minus.setStyleSheet("min-height:20;  \n"
                                     "border-style:solid;\n"
                                     "border-top-left-radius:2px;   \n"
                                     "border-top-right-radius:2px;\n"
                                     "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_minus.setIcon(icon)
        self.btn_minus.setIconSize(QtCore.QSize(30, 30))
        self.btn_minus.setFlat(True)
        self.btn_minus.setObjectName("minus")
        self.btn_minus.clicked.connect(self.showMinimized)
        self.horizontalLayout_5.addWidget(self.btn_minus)
        self.btn_max = QtWidgets.QPushButton(self.centralWidget)
        self.btn_max.setStyleSheet("border-radius:17px;padding:1px 1px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/maximize_window.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_max.setIcon(icon1)
        self.btn_max.setIconSize(QtCore.QSize(24, 24))
        self.btn_max.setObjectName("max")
        self.btn_max.clicked.connect(self.setMax)
        self.horizontalLayout_5.addWidget(self.btn_max)
        self.btn_close = QtWidgets.QPushButton(self.centralWidget)
        self.btn_close.setStyleSheet("border-radius:17px;padding:1px 1px")
        self.btn_close.setObjectName("close")
        icon2 = QtGui.QIcon(":/close21.png")
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QtCore.QSize(40, 40))
        self.btn_close.clicked.connect(self.resetClose)
        self.horizontalLayout_5.addWidget(self.btn_close)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        # 信息
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.led_information = QtWidgets.QLineEdit(self.centralWidget)
        self.led_information.setObjectName("led_information")
        self.horizontalLayout_8.addWidget(self.led_information)
        self.btn_ask = QtWidgets.QPushButton(self.centralWidget)
        self.btn_ask.setStyleSheet("border:2px groove gray;")
        self.btn_ask.setObjectName("btn_ask")
        self.btn_ask.setEnabled(False)
        self.btn_ask.clicked.connect(self.ask)
        self.horizontalLayout_8.addWidget(self.btn_ask)

        # 定时器和时钟
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.onTimerOut)
        self.lcd_clock = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcd_clock.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_clock.setObjectName("lcd_clock")
        self.lcd_clock.setDigitCount(10)
        self.lcd_clock.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcd_clock.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_clock.display(time.strftime("%X", time.localtime()))
        self.horizontalLayout_8.addWidget(self.lcd_clock)
        self.horizontalLayout_8.setStretch(0, 6)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        # 显示网页
        self.webView = QtWebEngineWidgets.QWebEngineView(self.widget)
        self.webView.setObjectName("webView")
        self.webView.setUrl(QtCore.QUrl('https://www.baidu.com'))
        self.listOfTask.currentIndexChanged.connect(self.vewWeb)
        self.verticalLayout_4.addWidget(self.webView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_numOfTask = QtWidgets.QLabel(self.centralWidget)
        self.lbl_numOfTask.setObjectName("lbl_numOfTask")
        self.horizontalLayout.addWidget(self.lbl_numOfTask)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setSpacing(0)

        # 传送文件
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.led_fileName = QtWidgets.QLineEdit(self.centralWidget)
        self.led_fileName.setStyleSheet("")
        self.led_fileName.setObjectName("led_fileName")
        self.horizontalLayout_3.addWidget(self.led_fileName)
        self.btn_getFile = QtWidgets.QPushButton(self.centralWidget)
        self.btn_getFile.setStyleSheet("border:2px groove gray;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../图片/Folder Open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_getFile.setIcon(icon3)
        self.btn_getFile.setObjectName("btn_getFile")
        self.btn_getFile.clicked.connect(self.openFile)
        self.horizontalLayout_3.addWidget(self.btn_getFile)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.line_4 = QtWidgets.QFrame(self.centralWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_3.addWidget(self.line_4)
        self.horizontalLayout_3.setStretch(0, 6)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 4)
        self.horizontalLayout_3.setStretch(4, 4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cmb_language = QtWidgets.QComboBox(self.centralWidget)
        self.cmb_language.setStyleSheet("border:2px groove gray;")
        self.cmb_language.setObjectName("cmb_language")
        self.cmb_language.addItem("")
        self.cmb_language.addItem("")
        self.cmb_language.addItem("")
        self.horizontalLayout_4.addWidget(self.cmb_language)
        self.btn_load = QtWidgets.QPushButton(self.centralWidget)
        self.btn_load.setStyleSheet("border:2px groove gray;")
        self.btn_load.setObjectName("btn_load")
        self.btn_load.setEnabled(False)
        self.btn_load.clicked.connect(self.send_file)
        self.horizontalLayout_4.addWidget(self.btn_load)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_4.setStretch(0, 6)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 4)
        self.horizontalLayout_4.setStretch(4, 2)
        self.horizontalLayout_4.setStretch(6, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 13)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_server.setText(_translate("MainWindow", "server"))
        self.lbl_Id.setText(_translate("MainWindow", "Id"))
        self.lbl_pwd.setText(_translate("MainWindow", "pwd"))
        self.btn_login.setText(_translate("MainWindow", "login"))
        self.btn_signUp.setText(_translate("MainWindow", "sign up"))
        self.led_information.setText(_translate("MainWindow", "information"))
        self.btn_ask.setText(_translate("MainWindow", "ask"))
        self.lbl_numOfTask.setText(_translate("MainWindow", "numberOfTask"))
        self.btn_getFile.setText(_translate("MainWindow", "file"))
        self.cmb_language.setItemText(0, _translate("MainWindow", "C++"))
        self.cmb_language.setItemText(1, _translate("MainWindow", "Java"))
        self.cmb_language.setItemText(2, _translate("MainWindow", "Python"))
        self.btn_load.setText(_translate("MainWindow", "load"))

    # zui da hua
    def setMax(self):
        self.btn_max.clicked.connect(self.setNormal)
        return self.showMaximized()

    # zheng chang hua
    def setNormal(self):
        self.btn_max.clicked.connect(self.setMax)
        return self.showNormal()

    # she zhi IP
    def showIPWin(self):
        winIP = IP.Ui_IP()
        winIP.show()
        winIP._signal.connect(self.setIP)
        winIP.exec_()

    def setIP(self, ip):
        self.IP = ip

    def Recv(self, sock, test):
        while True:
            msg = sock.recv(1024)
            msgList = msg.decode().split(',')
            if msgList[0] == 'yes':
                taskList = msgList[1].split(';')
                self.btn_ask.setEnabled(True)
                self.btn_load.setEnabled(True)
                self.btn_getTask.setEnabled(True)
                for i in range(0,len(taskList) - 1):
                    self.listOfTask.addItem(taskList[i])
                break
                # for i in range(0,len(self.taskList) - 1):
                #     self.listOfTask.addItem(self.taskList[i])

    def login(self):
        # chuang jian socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.connect((self.IP, self.port2))
        self.id = self.led_Id.text()
        data = '0;' + self.id + ';' + self.led_pwd.text()
        self.sock.send(bytes(data, 'utf-8'))

        self.recv = threading.Thread(target=self.Recv, args=(self.sock, None))
        self.recv.start()

    def resetClose(self):
        # if self.conn:
        #     self.conn.close()
        if self.sock:
            self.sock.close()

        return self.close()

    def signUp(self):
        winSignUp = SignUp.Ui_SignUp(self.sock)
        winSignUp.show()
        winSignUp.exec_()

    # def getTask(self):
    #     # No.2
    #     self.sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    #     self.sock1.connect((self.IP, self.port2))
    #     self.sock1.send(bytes('2;' + self.id,'utf-8'))
    #
    #     self.recv1 = threading.Thread(target=self.Recv, args=(self.sock1, None))
    #     self.recv1.start()

    def openFile(self):
        self.sock.send(bytes('2','utf-8'))
        fileName = QtWidgets.QFileDialog.getOpenFileName()
        if fileName:
            self.led_fileName.setText(fileName[0])
        else:
            self.led_fileName.setText("")

    def get_header(self,fileName):
        leng = len(fileName)
        assert leng < 250
        return chr(leng) + fileName

    def send_file(self):
        self.sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock1.connect((self.IP, self.port1))
        fileName = self.led_fileName.text()
        print(fileName)
        baseName = os.path.basename(fileName)
        header = bytes(self.get_header(baseName), 'utf-8')
        cont = bytes(open(fileName).read(), 'utf-8')
        self.sock1.sendall(header)
        self.sock1.sendall(cont)

    def ask(self):
        # No.4
        winChat = Chat.Ui_Chat(self.id,self.IP,self.port3)
        winChat.createThread()
        winChat.show()
        winChat.exec_()

    def onTimerOut(self):
        self.lcd_clock.display(time.strftime("%X", time.localtime()))

    def vewWeb(self,url):
        self.webView.load(QtCore.QUrl(self.listOfTask.currentText()))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_ACM()
    win.show()

    sys.exit(app.exec_())
