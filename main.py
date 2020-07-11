# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
# 
# Copyright 2020 by Ajeng Fitria Rahmawati

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
import sqlite3
from afterlogin import *

class Homepage(QWidget):
    #def __init__(self):
        #super().__init__()
        #self.setupUi(MainPage)

    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.resize(785, 551)
        self.centralwidget = QWidget(MainPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setGeometry(QRect(-20, -8, 821, 381))
        font = QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(85, 85, 127);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.Login = QTabWidget(self.centralwidget)
        self.Login.setGeometry(QRect(0, 80, 791, 431))
        self.Login.setMinimumSize(QSize(761, 431))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Login.setFont(font)
        self.Login.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(85, 85, 255);")
        self.Login.setObjectName("Login")
        self.Menu = QWidget()
        self.Menu.setObjectName("Menu")
        self.label = QLabel(self.Menu)
        self.label.setGeometry(QRect(370, 20, 301, 51))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.btnHomeCari = QPushButton(self.Menu)
        self.btnHomeCari.setGeometry(QRect(370, 320, 351, 41))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnHomeCari.setFont(font)
        self.btnHomeCari.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 255);")
        self.btnHomeCari.setObjectName("btnHomeCari")
        #--------------link cari--------------#
        self.btnHomeCari.clicked.connect(self.toTabLogin)

        self.layoutWidget = QWidget(self.Menu)
        self.layoutWidget.setGeometry(QRect(370, 100, 351, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_18 = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.label_7 = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_19 = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        self.label_8 = QLabel(self.Menu)
        self.label_8.setGeometry(QRect(0, 100, 311, 221))
        self.label_8.setStyleSheet("image: url(img/image 372.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.layoutWidget1 = QWidget(self.Menu)
        self.layoutWidget1.setGeometry(QRect(300, 100, 61, 201))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_29 = QLabel(self.layoutWidget1)
        self.label_29.setStyleSheet("image: url(img/wallet.png);")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.verticalLayout_7.addWidget(self.label_29)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setStyleSheet("image: url(img/startup.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setStyleSheet("image: url(img/work.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.label_21 = QLabel(self.layoutWidget1)
        self.label_21.setStyleSheet("image: url(img/world.png);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_7.addWidget(self.label_21)
        self.label_28 = QLabel(self.Menu)
        self.label_28.setGeometry(QRect(10, 130, 271, 191))
        self.label_28.setStyleSheet("image: url(img/City.png);")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.label_3 = QLabel(self.Menu)
        self.label_3.setGeometry(QRect(20, 90, 251, 71))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        #-----------tampilan tab Homepage----------#
        self.Login.addTab(self.Menu, "")
        self.Menu_2 = QWidget()
        self.Menu_2.setObjectName("Menu_2")
        self.label_5 = QLabel(self.Menu_2)
        self.label_5.setGeometry(QRect(380, 10, 301, 41))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.btnDaftar = QPushButton(self.Menu_2)
        self.btnDaftar.setGeometry(QRect(330, 350, 401, 41))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnDaftar.setFont(font)
        self.btnDaftar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 255);")
        self.btnDaftar.setObjectName("btnDaftar")
        #--------------link daftar--------------#
        self.btnDaftar.clicked.connect(self.addAkun)

        self.layoutWidget2 = QWidget(self.Menu_2)
        self.layoutWidget2.setGeometry(QRect(330, 80, 91, 221))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QLabel(self.layoutWidget2)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QLabel(self.layoutWidget2)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QLabel(self.layoutWidget2)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_13 = QLabel(self.layoutWidget2)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_14 = QLabel(self.layoutWidget2)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_12 = QLabel(self.layoutWidget2)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.layoutWidget_2 = QWidget(self.Menu_2)
        self.layoutWidget_2.setGeometry(QRect(430, 280, 301, 26))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radL = QRadioButton(self.layoutWidget_2)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radL.setFont(font)
        self.radL.setStyleSheet("color: rgb(255, 255, 255);")
        self.radL.setObjectName("radL")
        self.horizontalLayout.addWidget(self.radL)
        self.radP = QRadioButton(self.layoutWidget_2)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radP.setFont(font)
        self.radP.setStyleSheet("color: rgb(255, 255, 255);")
        self.radP.setObjectName("radP")
        self.horizontalLayout.addWidget(self.radP)
        self.layoutWidget_3 = QWidget(self.Menu_2)
        self.layoutWidget_3.setGeometry(QRect(430, 80, 301, 191))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.daftarNama = QLineEdit(self.layoutWidget_3)
        font = QFont()
        font.setFamily("Segoe UI Light")
        self.daftarNama.setFont(font)
        self.daftarNama.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.daftarNama.setObjectName("daftarNama")
        self.verticalLayout.addWidget(self.daftarNama)
        self.daftarEmail = QLineEdit(self.layoutWidget_3)
        font = QFont()
        font.setFamily("Segoe UI Light")
        self.daftarEmail.setFont(font)
        self.daftarEmail.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.daftarEmail.setObjectName("daftarEmail")
        self.verticalLayout.addWidget(self.daftarEmail)
        self.daftarPassword = QLineEdit(self.layoutWidget_3)
        font = QFont()
        font.setFamily("Segoe UI Light")
        self.daftarPassword.setFont(font)
        self.daftarPassword.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.daftarPassword.setEchoMode(QLineEdit.Password)
        self.daftarPassword.setObjectName("daftarPassword")
        self.verticalLayout.addWidget(self.daftarPassword)
        self.daftarAlamat = QLineEdit(self.layoutWidget_3)
        font = QFont()
        font.setFamily("Segoe UI Light")
        self.daftarAlamat.setFont(font)
        self.daftarAlamat.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.daftarAlamat.setObjectName("daftarAlamat")
        self.verticalLayout.addWidget(self.daftarAlamat)
        self.daftarHp = QLineEdit(self.layoutWidget_3)
        font = QFont()
        font.setFamily("Segoe UI Light")
        self.daftarHp.setFont(font)
        self.daftarHp.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.daftarHp.setObjectName("daftarHp")
        self.verticalLayout.addWidget(self.daftarHp)
        self.checkData = QCheckBox(self.Menu_2)
        self.checkData.setGeometry(QRect(570, 320, 161, 17))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.checkData.setFont(font)
        self.checkData.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkData.setObjectName("checkData")
        self.label_15 = QLabel(self.Menu_2)
        self.label_15.setGeometry(QRect(20, 300, 301, 51))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.label_22 = QLabel(self.Menu_2)
        self.label_22.setGeometry(QRect(80, 170, 161, 20))
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_27 = QLabel(self.Menu_2)
        self.label_27.setGeometry(QRect(10, 70, 301, 211))
        self.label_27.setStyleSheet("image: url(img/signup.png);")
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")

        #-----------tampilan daftar / registrasi----------#
        self.Login.addTab(self.Menu_2, "")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.label_23 = QLabel(self.tab)
        self.label_23.setGeometry(QRect(290, 30, 211, 41))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.btnLogin = QPushButton(self.tab)
        self.btnLogin.setGeometry(QRect(240, 210, 331, 41))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 255);")
        self.btnLogin.setObjectName("btnLogin")
        #--------------link login--------------#
        self.btnLogin.clicked.connect(self.login)

        self.label_26 = QLabel(self.tab)
        self.label_26.setGeometry(QRect(240, 270, 241, 21))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_26.setObjectName("label_26")
        self.btnBuat = QPushButton(self.tab)
        self.btnBuat.setGeometry(QRect(440, 260, 131, 41))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnBuat.setFont(font)
        self.btnBuat.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 255);")
        self.btnBuat.setObjectName("btnBuat")
        #--------------link belum punya akun--------------#
        self.btnBuat.clicked.connect(self.toTabDaftar)


        self.layoutWidget3 = QWidget(self.tab)
        self.layoutWidget3.setGeometry(QRect(340, 110, 231, 91))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.loginEmail = QLineEdit(self.layoutWidget3)
        font = QFont()
        font.setFamily("Segoe UI Light")
        self.loginEmail.setFont(font)
        self.loginEmail.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.loginEmail.setObjectName("loginEmail")
        self.verticalLayout_5.addWidget(self.loginEmail)
        self.loginPassword = QLineEdit(self.layoutWidget3)
        font = QFont()
        font.setFamily("Segoe UI Light")
        self.loginPassword.setFont(font)
        self.loginPassword.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.loginPassword.setEchoMode(QLineEdit.Password)
        self.loginPassword.setObjectName("loginPassword")
        self.verticalLayout_5.addWidget(self.loginPassword)
        self.layoutWidget4 = QWidget(self.tab)
        self.layoutWidget4.setGeometry(QRect(240, 120, 88, 71))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_24 = QLabel(self.layoutWidget4)
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_6.addWidget(self.label_24)
        self.label_25 = QLabel(self.layoutWidget4)
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_6.addWidget(self.label_25)

        #-----------tampilan tab log in----------#
        self.Login.addTab(self.tab, "")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setGeometry(QRect(320, 20, 171, 37))
        font = QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(85, 85, 255);")
        self.label_17.setObjectName("label_17")
        MainPage.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainPage)
        self.statusbar.setObjectName("statusbar")
        MainPage.setStatusBar(self.statusbar)

        self.retranslateUi(MainPage)
        self.Login.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QCoreApplication.translate
        MainPage.setWindowTitle(_translate("Homepage", "Homepage"))
        self.label.setText(_translate("MainPage", "Lowongan Kerja Indonesia"))
        self.btnHomeCari.setText(_translate("MainPage", "CARI LOKER SEKARANG"))
        self.label_6.setText(_translate("MainPage", "Bayar pendaftaran setelah terima Job"))
        self.label_18.setText(_translate("MainPage", "Perusahaan Berkualitas"))
        self.label_7.setText(_translate("MainPage", "Lowongan kerja beragam"))
        self.label_19.setText(_translate("MainPage", "Lowongan tersebar diberbagai Kota"))
        self.label_3.setText(_translate("MainPage", "LOKERINDO\n"
"Membantu menemukan karier\n"
"dengan mudah, hemat dan cepat"))
        self.Login.setTabText(self.Login.indexOf(self.Menu), _translate("MainPage", "                      Homepage                      "))
        self.label_5.setText(_translate("MainPage", "Silahkan Isi Data Anda"))
        self.btnDaftar.setText(_translate("MainPage", "DAFTAR"))
        self.label_9.setText(_translate("MainPage", "Nama"))
        self.label_10.setText(_translate("MainPage", "Email"))
        self.label_11.setText(_translate("MainPage", "Pasword"))
        self.label_13.setText(_translate("MainPage", "Alamat"))
        self.label_14.setText(_translate("MainPage", "No Hp"))
        self.label_12.setText(_translate("MainPage", "Gender"))
        self.radL.setText(_translate("MainPage", "Laki-laki"))
        self.radP.setText(_translate("MainPage", "Perempuan"))
        self.checkData.setText(_translate("MainPage", "Apakah Data Sudah Tepat ?"))
        self.label_15.setText(_translate("MainPage", "Segera daftar dan dapatkan job sesuai\n"
"            pasion dan keahlianmu"))
        self.Login.setTabText(self.Login.indexOf(self.Menu_2), _translate("MainPage", "                        Daftar                       ", " "))
        self.label_23.setText(_translate("MainPage", "Selamat Datang"))
        self.btnLogin.setText(_translate("MainPage", "Masuk"))
        self.label_26.setText(_translate("MainPage", "Belum memiliki akun ?"))
        self.btnBuat.setText(_translate("MainPage", "Buat Akun"))
        self.label_24.setText(_translate("MainPage", "Email"))
        self.label_25.setText(_translate("MainPage", "Pasword"))
        self.Login.setTabText(self.Login.indexOf(self.tab), _translate("MainPage", "                        Masuk                        "))
        self.label_17.setText(_translate("MainPage", "LOKERINDO"))

    #---------------------------FUNCTION------------------------#
    #-------------------registrasi-----------------#
    def addAkun(self):
        idAkun = self.getRowCountAkun(MainPage) + 1
        nama = self.daftarNama.text()
        email = self.daftarEmail.text()
        alamat = self.daftarAlamat.text()
        password = self.daftarPassword.text()
        nohp = int(self.daftarHp.text())
        if self.radP.isChecked() :
            gender = 'Perempuan'
        else :
            gender = 'Laki-laki'
        queryAddAkun = QSqlQuery()
        queryAddAkun.exec_("INSERT INTO akun VALUES (%d, '%s', '%s', '%s', '%s', %d, '%s', '', '', '')" %
                (idAkun, nama, email, alamat, password, nohp, gender))
        QMessageBox.information(self, 'Berhasil Registrasi', 'Anda berhasil melakukan registrasi, silahkan ke halaman login untuk masuk')
        self.Login.setCurrentIndex(2)

    #-------------------load jumlah baris akun----------------------#
    def getRowCountAkun(self, MainPage):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM akun')
        query.next()
        rowCount = query.value(0)
        return rowCount

    #-------------------------link ke tab login-------------------------#
    def toTabLogin(self, MainPage):
        self.Login.setCurrentIndex(2)

    #--------------------------link ke tab daftar-----------------------#
    def toTabDaftar(self, MainPage):
        self.Login.setCurrentIndex(1)

    #--------------------------login-----------------------#
    def login(self):
        email = self.loginEmail.text()
        password = self.loginPassword.text()
        conn = sqlite3.connect('Lokerindo')
        cursor = conn.cursor()
        cursor.execute('''SELECT email, pass FROM akun WHERE email = '%s' AND pass = '%s' ''' % (email, password))
        if cursor.fetchone():
            query1 = QSqlQuery()
            query1.exec_ ('''SELECT id FROM akun WHERE email = '%s' AND pass = '%s' ''' % (email, password))
            query1.next()
            getId = query1.value(0)

            #------------------akses afterlogin--------------#
            MainPage.close()
            
            Dialog = QDialog()
            self.form = Ui_Dialog()
            self.form.setupUi(Dialog)
            #self.form.getIdAkun(getId)
            self.form.loadProfile(getId)
            self.form.loadLamaran(getId)
            self.form.labelId.setText(str(getId))
            Dialog.show()
            Dialog.exec_()

        else:
            QMessageBox.warning(self, 'Login Gagal', 'Email dan password tidak sesuai')

    #--------------------id akun-------------------------#
    #def getIdAkun(self):
        #pass

    #---------------------akses Home----------------------#
    #def openHome(self, email):
        #MainPage.close()
        
        #MainWindow = QDialog()
        #self.form = Ui_Dialog()
        #self.form.setupUi(MainWindow)
        #MainWindow.show()
        #MainWindow.exec_()
        

if __name__ == "__main__":
    import sys
    app1 = QApplication(sys.argv)

    #---------------connect database----------------#
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('Lokerindo')
    if not db.open():
        print('ERROR: ' + db.lastError().text())
        sys.exit(1)

    #---------------menjalankan gui----------------#
    MainPage = QMainWindow()
    ui = Homepage()
    ui.setupUi(MainPage)
    MainPage.show()
    app1.exec_()
