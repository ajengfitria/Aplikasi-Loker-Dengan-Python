# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.loadDataLoker()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(785, 569)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setGeometry(QRect(-90, 0, 881, 551))
        font = QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(85, 85, 127);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setGeometry(QRect(310, 20, 171, 51))
        font = QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(85, 85, 255);")
        self.label_17.setObjectName("label_17")
        self.Home_2 = QTabWidget(self.centralwidget)
        self.Home_2.setGeometry(QRect(0, 90, 791, 431))
        self.Home_2.setMinimumSize(QSize(791, 431))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Home_2.setFont(font)
        self.Home_2.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(85, 85, 255);")
        self.Home_2.setObjectName("Home_2")
        self.Home = QWidget()
        self.Home.setObjectName("Home")
        self.label_5 = QLabel(self.Home)
        self.label_5.setGeometry(QRect(80, 20, 481, 41))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_22 = QLabel(self.Home)
        self.label_22.setGeometry(QRect(80, 170, 161, 20))
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.tLowongan = QTableWidget(self.Home)
        self.tLowongan.setGeometry(QRect(80, 70, 621, 261))
        font = QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tLowongan.setFont(font)
        self.tLowongan.setStyleSheet("color: rgb(85, 85, 255);\n"
"background-color: white;")
        self.tLowongan.setObjectName("tLowongan")

        self.Home_2.addTab(self.Home, "")
        self.Profile = QWidget()
        self.Profile.setObjectName("Profile")
        self.label_33 = QLabel(self.Profile)
        self.label_33.setGeometry(QRect(30, 40, 101, 91))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_33.setObjectName("label_33")
        self.widget = QWidget(self.Profile)
        self.widget.setGeometry(QRect(140, 40, 301, 303))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QLabel(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_15 = QLabel(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 5, 0, 1, 1)
        self.label_12 = QLabel(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 3, 0, 1, 1)
        self.radL = QRadioButton(self.widget)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radL.setFont(font)
        self.radL.setStyleSheet("color: rgb(255, 255, 255);")
        self.radL.setObjectName("radL")
        self.gridLayout_3.addWidget(self.radL, 5, 2, 1, 1)
        self.radP = QRadioButton(self.widget)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radP.setFont(font)
        self.radP.setStyleSheet("color: rgb(255, 255, 255);")
        self.radP.setObjectName("radP")
        self.gridLayout_3.addWidget(self.radP, 5, 1, 1, 1)
        self.pAlamat = QTextEdit(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        self.pAlamat.setFont(font)
        self.pAlamat.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pAlamat.setObjectName("pAlamat")
        self.gridLayout_3.addWidget(self.pAlamat, 2, 1, 1, 2)
        self.label_9 = QLabel(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.pPassword = QLineEdit(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        self.pPassword.setFont(font)
        self.pPassword.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pPassword.setObjectName("pPassword")
        self.gridLayout_3.addWidget(self.pPassword, 3, 1, 1, 2)
        self.label_13 = QLabel(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_10 = QLabel(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.pNama = QLineEdit(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        self.pNama.setFont(font)
        self.pNama.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pNama.setText("")
        self.pNama.setObjectName("pNama")
        self.gridLayout_3.addWidget(self.pNama, 0, 1, 1, 2)
        self.pEmail = QLineEdit(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        self.pEmail.setFont(font)
        self.pEmail.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pEmail.setObjectName("pEmail")
        self.gridLayout_3.addWidget(self.pEmail, 1, 1, 1, 2)
        self.pHp = QLineEdit(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        self.pHp.setFont(font)
        self.pHp.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pHp.setObjectName("pHp")
        self.gridLayout_3.addWidget(self.pHp, 4, 1, 1, 2)
        self.label_19 = QLabel(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 6, 0, 1, 1)
        self.pHp_2 = QLineEdit(self.widget)
        font = QFont()
        font.setFamily("Segoe UI")
        self.pHp_2.setFont(font)
        self.pHp_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pHp_2.setObjectName("pHp_2")
        self.gridLayout_3.addWidget(self.pHp_2, 6, 1, 1, 2)
        self.btnSimpanProfile = QPushButton(self.Profile)
        self.btnSimpanProfile.setGeometry(QRect(580, 270, 152, 31))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btnSimpanProfile.setFont(font)
        self.btnSimpanProfile.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 255);")
        self.btnSimpanProfile.setObjectName("btnSimpanProfile")
        self.widget1 = QWidget(self.Profile)
        self.widget1.setGeometry(QRect(470, 40, 258, 211))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QLabel(self.widget1)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.pPengalaman = QTextEdit(self.widget1)
        font = QFont()
        font.setFamily("Segoe UI")
        self.pPengalaman.setFont(font)
        self.pPengalaman.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pPengalaman.setObjectName("pPengalaman")
        self.gridLayout_2.addWidget(self.pPengalaman, 1, 0, 1, 1)
        self.label_18 = QLabel(self.widget1)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 2, 0, 1, 1)
        self.pSkill = QTextEdit(self.widget1)
        font = QFont()
        font.setFamily("Segoe UI")
        self.pSkill.setFont(font)
        self.pSkill.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pSkill.setObjectName("pSkill")
        self.gridLayout_2.addWidget(self.pSkill, 3, 0, 1, 1)
        self.Home_2.addTab(self.Profile, "")
        self.Lamaran = QWidget()
        self.Lamaran.setObjectName("Lamaran")
        self.label_27 = QLabel(self.Lamaran)
        self.label_27.setGeometry(QRect(80, 90, 241, 231))
        self.label_27.setStyleSheet("image: url(img/signup.png);")
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.layoutWidget = QWidget(self.Lamaran)
        self.layoutWidget.setGeometry(QRect(371, 112, 252, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_34 = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 0, 0, 1, 1)
        self.subNo = QLineEdit(self.layoutWidget)
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.subNo.setFont(font)
        self.subNo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.subNo.setText("")
        self.subNo.setObjectName("subNo")
        self.gridLayout.addWidget(self.subNo, 0, 1, 1, 1)
        self.label_35 = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 1, 0, 1, 1)
        self.btnUnggahCV = QPushButton(self.layoutWidget)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnUnggahCV.setFont(font)
        self.btnUnggahCV.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 255);")
        self.btnUnggahCV.setObjectName("btnUnggahCV")
        self.gridLayout.addWidget(self.btnUnggahCV, 1, 1, 1, 1)
        self.btnSubmitLamaran = QPushButton(self.layoutWidget)
        font = QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btnSubmitLamaran.setFont(font)
        self.btnSubmitLamaran.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 255);")
        self.btnSubmitLamaran.setObjectName("btnSubmitLamaran")
        self.gridLayout.addWidget(self.btnSubmitLamaran, 2, 0, 1, 2)
        self.label_36 = QLabel(self.Lamaran)
        self.label_36.setGeometry(QRect(370, 220, 251, 25))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_36.setObjectName("label_36")
        self.Home_2.addTab(self.Lamaran, "")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.label_6 = QLabel(self.tab)
        self.label_6.setGeometry(QRect(80, 20, 451, 41))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.t_lamaran = QTableWidget(self.tab)
        self.t_lamaran.setGeometry(QRect(80, 70, 621, 261))
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.t_lamaran.setFont(font)
        self.t_lamaran.setStyleSheet("color: rgb(85, 85, 255);\n"
"background-color: rgb(227, 227, 227);")
        self.t_lamaran.setRowCount(11)
        self.t_lamaran.setColumnCount(6)
        self.t_lamaran.setObjectName("t_lamaran")
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Segoe UI Light")
        item.setFont(font)
        self.t_lamaran.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        item.setFont(font)
        self.t_lamaran.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        item.setFont(font)
        self.t_lamaran.setVerticalHeaderItem(2, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        item.setFont(font)
        self.t_lamaran.setVerticalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.t_lamaran.setVerticalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.t_lamaran.setVerticalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.t_lamaran.setVerticalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.t_lamaran.setVerticalHeaderItem(7, item)
        item = QTableWidgetItem()
        self.t_lamaran.setVerticalHeaderItem(8, item)
        item = QTableWidgetItem()
        self.t_lamaran.setVerticalHeaderItem(9, item)
        item = QTableWidgetItem()
        self.t_lamaran.setVerticalHeaderItem(10, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t_lamaran.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t_lamaran.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t_lamaran.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t_lamaran.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t_lamaran.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t_lamaran.setHorizontalHeaderItem(5, item)
        self.Home_2.addTab(self.tab, "")
        self.btnLogout = QPushButton(self.centralwidget)
        self.btnLogout.setGeometry(QRect(700, 90, 91, 31))
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogout.setFont(font)
        self.btnLogout.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.btnLogout.setObjectName("btnLogout")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Home_2.setCurrentIndex(2)
        self.btnLogout.clicked.connect(self.close)
        QMetaObject.connectSlotsByName(MainWindow)

        layout = QVBoxLayout()
        layout.addWidget(self.tLowongan)
        self.setLayout(layout)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Lokerindo", "Lokerindo"))
        self.label_17.setText(_translate("MainWindow", "LOKERINDO"))
        self.label_5.setText(_translate("MainWindow", "Ayo, cari pekerjaan sesuai keahlian kamu di sini....!"))
        #item = self.tLowongan.horizontalHeaderItem(0)
        #item.setText(_translate("MainWindow", "No"))
        #item = self.tLowongan.horizontalHeaderItem(1)
        #item.setText(_translate("MainWindow", "Posisi"))
        #item = self.tLowongan.horizontalHeaderItem(2)
        #item.setText(_translate("MainWindow", "Perusahaan"))
        #item = self.tLowongan.horizontalHeaderItem(3)
        #item.setText(_translate("MainWindow", "Penempatan"))
        #item = self.tLowongan.horizontalHeaderItem(4)
        #item.setText(_translate("MainWindow", "Gaji Ditawarkan"))
        #item = self.tLowongan.horizontalHeaderItem(5)
        #item.setText(_translate("MainWindow", "Max Submit"))
        self.Home_2.setTabText(self.Home_2.indexOf(self.Home), _translate("MainWindow", "             Home          ", " "))
        self.label_33.setText(_translate("MainWindow", "     Foto"))
        self.label_14.setText(_translate("MainWindow", "No Hp"))
        self.label_15.setText(_translate("MainWindow", "Gender"))
        self.label_12.setText(_translate("MainWindow", "Pasword"))
        self.radL.setText(_translate("MainWindow", "Laki-laki"))
        self.radP.setText(_translate("MainWindow", "Perempuan"))
        self.label_9.setText(_translate("MainWindow", "Email"))
        self.label_13.setText(_translate("MainWindow", "Nama"))
        self.label_10.setText(_translate("MainWindow", "Alamat"))
        self.label_19.setText(_translate("MainWindow", "Pekerjaan"))
        self.btnSimpanProfile.setText(_translate("MainWindow", "Simpan Perubahan"))
        self.label_11.setText(_translate("MainWindow", "Pengalaman Kerja"))
        self.label_18.setText(_translate("MainWindow", "Keahlian"))
        self.Home_2.setTabText(self.Home_2.indexOf(self.Profile), _translate("MainWindow", "             Profile             "))
        self.label_34.setText(_translate("MainWindow", "No Lowongan"))
        self.label_35.setText(_translate("MainWindow", "Unggah CV"))
        self.btnUnggahCV.setText(_translate("MainWindow", "Unggah CV"))
        self.btnSubmitLamaran.setText(_translate("MainWindow", "Submit"))
        self.label_36.setText(_translate("MainWindow", "**Lihat nomor lowongan di menu home"))
        self.Home_2.setTabText(self.Home_2.indexOf(self.Lamaran), _translate("MainWindow", "        Submit Lamaran        "))
        self.label_6.setText(_translate("MainWindow", "Lihat kemajuan lamaran kamu.."))
        item = self.t_lamaran.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No"))
        item = self.t_lamaran.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Posisi"))
        item = self.t_lamaran.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Perusahaan"))
        item = self.t_lamaran.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Penempatan"))
        item = self.t_lamaran.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tgl Submit"))
        item = self.t_lamaran.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Status"))
        self.Home_2.setTabText(self.Home_2.indexOf(self.tab), _translate("MainWindow", "       Daftar Lamaran      "))
        self.btnLogout.setText(_translate("MainWindow", "Keluar"))


    def loadDataLoker(self):
        self.tLowongan.clear()
        self.tLowongan.setRowCount(self.getRowCountLoker())
        self.tLowongan.setColumnCount(6)
        columnHeaders = ['No', 'Posisi', 'Perusahaan','Penempatan','Gaji Ditawarkan','Max Submit']
        self.tLowongan.setHorizontalHeaderLabels(columnHeaders)
        query = QSqlQuery()
        no, posisi, perusahaan, penempatan, gaji, deadline = range(6)
        row = 0
        query.exec_('SELECT * FROM loker')
        while query.next() :
            for i in range(6):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.tLowongan.setItem(row, i, item)
            row += 1
        item = QTableWidgetItem()
        item.setText(str(self.getRowCountLoker()))
        self.tLowongan.setItem(6, 0, item)

    def getRowCountLoker(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM loker')
        query.next()
        rowCount = query.value(0)
        return rowCount


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('Lokerindo')
    if not db.open():
        print('ERROR: ' + db.lastError().text())
        sys.exit(1)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.show()
    sys.exit(app.exec_())