# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_btn = QtWidgets.QCheckBox(self.centralwidget)
        self.open_btn.setGeometry(QtCore.QRect(160, 190, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.open_btn.setFont(font)
        self.open_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.open_btn.setIconSize(QtCore.QSize(30, 30))
        self.open_btn.setCheckable(True)
        self.open_btn.setChecked(False)
        self.open_btn.setAutoRepeat(False)
        self.open_btn.setAutoExclusive(False)
        self.open_btn.setTristate(False)
        self.open_btn.setObjectName("open_btn")
        self.statue = QtWidgets.QLabel(self.centralwidget)
        self.statue.setGeometry(QtCore.QRect(120, 20, 191, 91))
        self.statue.setAlignment(QtCore.Qt.AlignCenter)
        self.statue.setObjectName("statue")
        self.dialog_statue = QtWidgets.QLabel(self.centralwidget)
        self.dialog_statue.setGeometry(QtCore.QRect(350, 190, 171, 71))
        self.dialog_statue.setText("")
        self.dialog_statue.setAlignment(QtCore.Qt.AlignCenter)
        self.dialog_statue.setObjectName("dialog_statue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 36))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_btn.setText(_translate("MainWindow", "开始识别"))
        self.statue.setText(_translate("MainWindow", "暂未开始识别"))
