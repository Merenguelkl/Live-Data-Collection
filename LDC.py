# -*- coding: utf-8 -*-
import ctypes
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

import info

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1134, 602)
        MainWindow.setMaximumSize(QtCore.QSize(1300, 615))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.tabWidget.setMinimumSize(QtCore.QSize(3, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 800, 590))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(0, 0, 800, 590))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(0, 0, 800, 590))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(0, 0, 800, 590))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(0, 0, 800, 590))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.tab_6)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(0, 0, 800, 590))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.tab_7)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(0, 0, 800, 590))
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.tab_8)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(0, 0, 800, 590))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.plainTextEdit_9 = QtWidgets.QPlainTextEdit(self.tab_9)
        self.plainTextEdit_9.setGeometry(QtCore.QRect(0, 0, 800, 590))
        self.plainTextEdit_9.setObjectName("plainTextEdit_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.plainTextEdit_10 = QtWidgets.QPlainTextEdit(self.tab_10)
        self.plainTextEdit_10.setGeometry(QtCore.QRect(0, 0, 800, 590))
        self.plainTextEdit_10.setObjectName("plainTextEdit_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(845, 110, 44, 34))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(845, 156, 43, 34))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(830, 20, 271, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(810, 575, 361, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(904, 156, 231, 34))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(924, 110, 231, 34))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(902, 556, 231, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(820, 50, 291, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(844, 140, 241, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(844, 190, 241, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(880, 470, 171, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(840, 240, 248, 197))
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # 更新文本内容
        self.retranslateUi(MainWindow)

        # 设置计时器自动更新时间
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 更新时间
    def update(self):
        TimeDate = QDateTime.currentDateTime()
        timeDisplay = TimeDate.toString("hh:mm:ss")
        self.label_3.setText(timeDisplay)

    # 更新文本内容
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Live Data Collection By 57117137刘康亮"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", info.get_sys_info()))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "OS Info"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", info.get_user_info()))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "User Info"))
        self.plainTextEdit_3.setPlainText(_translate("MainWindow", info.get_nic_info()))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "NIC Info"))
        self.plainTextEdit_4.setPlainText(_translate("MainWindow", info.get_routing_info()))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Routing Info"))
        self.plainTextEdit_5.setPlainText(_translate("MainWindow", info.get_conn_info()))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Conn Info"))
        self.plainTextEdit_6.setPlainText(_translate("MainWindow", info.get_arp_info()))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Arp Info"))
        self.plainTextEdit_7.setPlainText(_translate("MainWindow", info.get_disk_info()))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Disk Info"))
        self.plainTextEdit_8.setPlainText(_translate("MainWindow", info.get_file_handle()))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Handle"))
        self.plainTextEdit_9.setPlainText(_translate("MainWindow", info.get_process_info()))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Process"))
        self.plainTextEdit_10.setPlainText(_translate("MainWindow", info.get_service_info()))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Service"))
        self.label.setText(_translate("MainWindow", "Time:"))
        self.label_2.setText(_translate("MainWindow", "Date:"))
        self.label_5.setText(_translate("MainWindow", "Live Data Collection"))
        self.label_6.setText(_translate("MainWindow", "Copyright © 2020 Kangliang Liu. All rights reserved."))
        self.label_4.setText(_translate("MainWindow", info.get_date()))
        self.label_7.setText(_translate("MainWindow", "Southeast University, Nanjing, China"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./finger.ico"))
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
