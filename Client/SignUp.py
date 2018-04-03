# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sourceSignUp,sys,pymysql,socket,IP

class Ui_SignUp(QtWidgets.QMainWindow):

    def __init__(self,sock):
        super(Ui_SignUp, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.sock = sock
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
        MainWindow.resize(352, 169)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setStyleSheet("background-color: rgb(233, 255, 255);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 0, 9, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_minus = QtWidgets.QPushButton(self.centralWidget)
        self.btn_minus.setStyleSheet("min-height:20;  \n"
"border-style:solid;\n"
"border-top-left-radius:2px;   \n"
"border-top-right-radius:2px;\n"
"")
        self.btn_minus.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minus.setIcon(icon)
        self.btn_minus.setIconSize(QtCore.QSize(25, 25))
        self.btn_minus.setFlat(False)
        self.btn_minus.setObjectName("btn_minus")
        self.btn_minus.clicked.connect(self.showMinimized)
        self.horizontalLayout.addWidget(self.btn_minus)
        self.btn_close = QtWidgets.QPushButton(self.centralWidget)
        self.btn_close.setStyleSheet("min-height:20;  \n"
"border-style:solid;\n"
"border-top-left-radius:2px;   \n"
"border-top-right-radius:2px;\n"
"")
        self.btn_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/prefix1/close21.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QtCore.QSize(32, 32))
        self.btn_close.setObjectName("btn_close")
        self.btn_close.clicked.connect(self.reClose)
        self.horizontalLayout.addWidget(self.btn_close)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_pwd = QtWidgets.QLabel(self.centralWidget)
        self.lbl_pwd.setObjectName("lbl_pwd")
        self.gridLayout.addWidget(self.lbl_pwd, 1, 0, 1, 1)
        self.led_pwd = QtWidgets.QLineEdit(self.centralWidget)
        self.led_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.led_pwd.setObjectName("led_pwd")
        self.gridLayout.addWidget(self.led_pwd, 1, 1, 1, 1)
        self.led_ID = QtWidgets.QLineEdit(self.centralWidget)
        self.led_ID.setObjectName("led_ID")
        self.gridLayout.addWidget(self.led_ID, 0, 1, 1, 1)
        self.lbl_ID = QtWidgets.QLabel(self.centralWidget)
        self.lbl_ID.setObjectName("lbl_ID")
        self.gridLayout.addWidget(self.lbl_ID, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_confirm = QtWidgets.QPushButton(self.centralWidget)
        self.btn_confirm.setObjectName("btn_confirm")
        self.btn_confirm.setStyleSheet("border:2px groove gray;")
        self.btn_confirm.clicked.connect(self.signUp)
        self.horizontalLayout_2.addWidget(self.btn_confirm)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_pwd.setText(_translate("MainWindow", "pwd"))
        self.led_pwd.setPlaceholderText(_translate("MainWindow", "max size is 6"))
        self.led_ID.setPlaceholderText(_translate("MainWindow", "max size is 6"))
        self.lbl_ID.setText(_translate("MainWindow", "ID"))
        self.btn_confirm.setText(_translate("MainWindow", "confirm"))

    def signUp(self):
        data = '1;' + self.led_ID.text() + ';' + self.led_pwd.text()

        self.sock.send(bytes(data,'utf-8'))
        print(self.s.recv(1024))
        self.sock.close()
        return self.close()

    def reClose(self):
        self.s.close()
        return self.close()


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#
#     win = Ui_SignUp()
#     win.show()
#
#     sys.exit(app.exec_())