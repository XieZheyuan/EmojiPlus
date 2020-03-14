# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emojji.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setWindowTitle("Emojii++")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 601, 391))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 420, 121, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_O = QtWidgets.QAction(MainWindow)
        self.action_O.setObjectName("action_O")
        self.action_I = QtWidgets.QAction(MainWindow)
        self.action_I.setObjectName("action_I")
        self.actionQuit_Q = QtWidgets.QAction(MainWindow)
        self.actionQuit_Q.setObjectName("actionQuit_Q")
        self.action_A = QtWidgets.QAction(MainWindow)
        self.action_A.setObjectName("action_A")
        self.actionQuit_Q_2 = QtWidgets.QAction(MainWindow)
        self.actionQuit_Q_2.setObjectName("actionQuit_Q_2")
        self.action_T = QtWidgets.QAction(MainWindow)
        self.action_T.setObjectName("action_T")
        self.action_Y = QtWidgets.QAction(MainWindow)
        self.action_Y.setObjectName("action_Y")
        self.menu_F.addAction(self.action_O)
        self.menu_F.addAction(self.action_I)
        self.menu_F.addAction(self.actionQuit_Q)
        self.menu_F.addAction(self.action_A)
        self.menu_F.addAction(self.actionQuit_Q_2)
        self.menu_E.addAction(self.action_T)
        self.menu_E.addAction(self.action_Y)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Untitled.emojji"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_E.setTitle(_translate("MainWindow", "插入(&E)"))
        self.action_O.setText(_translate("MainWindow", "打开(&O)"))
        self.action_O.setToolTip(_translate("MainWindow", "打开一个EMOJII文件"))
        self.action_O.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_I.setText(_translate("MainWindow", "打开来自图片(&I)"))
        self.action_I.setToolTip(_translate("MainWindow", "打开来自图片的文件"))
        self.action_I.setShortcut(_translate("MainWindow", "Alt+O"))
        self.actionQuit_Q.setText(_translate("MainWindow", "保存(&S)"))
        self.actionQuit_Q.setToolTip(_translate("MainWindow", "保存为EMOJII文件"))
        self.actionQuit_Q.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_A.setText(_translate("MainWindow", "另存为……(&A)"))
        self.action_A.setToolTip(_translate("MainWindow", "另存为EMOJII文件"))
        self.action_A.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionQuit_Q_2.setText(_translate("MainWindow", "Quit(&Q)"))
        self.action_T.setText(_translate("MainWindow", "特殊字符(&T)"))
        self.action_T.setToolTip(_translate("MainWindow", "打开特殊字符选项卡"))
        self.action_T.setShortcut(_translate("MainWindow", "Ctrl+Shift+T"))
        self.action_Y.setText(_translate("MainWindow", "颜文字模板(&Y)"))
        self.action_Y.setToolTip(_translate("MainWindow", "颜文字模板"))
        self.action_Y.setShortcut(_translate("MainWindow", "Ctrl+Shift+Y"))

