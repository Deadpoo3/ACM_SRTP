# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IP.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sourceIP
import sys,ACM

class Ui_IP(QtWidgets.QMainWindow):
    _signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Ui_IP,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.IP = ""

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
        MainWindow.resize(340, 50)
        MainWindow.setStyleSheet("background-color: rgb(233, 255, 255);")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_minus = QtWidgets.QPushButton(self.centralWidget)
        self.btn_minus.setStyleSheet("border-radius:17px;padding:1px 1px")
        self.btn_minus.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minus.setIcon(icon)
        self.btn_minus.setIconSize(QtCore.QSize(30, 30))
        self.btn_minus.setObjectName("btn_minus")
        self.btn_minus.clicked.connect(self.showMinimized)
        self.horizontalLayout_3.addWidget(self.btn_minus)
        self.btn_close = QtWidgets.QPushButton(self.centralWidget)
        self.btn_close.setStyleSheet("border-radius:17px;padding:1px 1px")
        self.btn_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/prefix1/close21.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QtCore.QSize(37, 37))
        self.btn_close.setObjectName("btn_close")
        self.btn_close.clicked.connect(self.close)
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_IP = QtWidgets.QLabel(self.centralWidget)
        self.lbl_IP.setObjectName("lbl_IP")
        self.horizontalLayout.addWidget(self.lbl_IP)
        self.led_IP = QtWidgets.QLineEdit(self.centralWidget)
        self.led_IP.setStyleSheet("border:2px groove gray;")
        self.led_IP.setObjectName("led_IP")
        self.horizontalLayout.addWidget(self.led_IP)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_confirm = QtWidgets.QPushButton(self.centralWidget)
        self.btn_confirm.setStyleSheet("border:2px groove gray;")
        self.btn_confirm.setObjectName("btn_confirm")
        self.btn_confirm.clicked.connect(self.resetClose)
        self.horizontalLayout_2.addWidget(self.btn_confirm)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 3)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_IP.setText(_translate("MainWindow", "IP"))
        self.btn_confirm.setText(_translate("MainWindow", "confirm"))

    def resetClose(self):
        self.IP = self.led_IP.text()
        self._signal.emit(self.IP)
        return self.close()
