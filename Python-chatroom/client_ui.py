# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatroom.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# Here is the chatroom_client's GUI setting file,
# I separate the setting of GUI from the original file,
# so that I can develope faster and more efficient
# When new .ui file is change into .py,
# just Copy and Paste the Ui_MainWindow or others has to be Pasted

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 850, 600))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 850, 350))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 350, 850, 250))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 750, 140))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(750, 0, 100, 140))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.toolBox = QtWidgets.QToolBox(self.tab_2)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 850, 300))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 850, 230))
        self.page.setObjectName("page")
        self.textEdit_3 = QtWidgets.QTextEdit(self.page)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 0, 850, 230))
        self.textEdit_3.setObjectName("textEdit_3")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 850, 230))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 25))
        self.menubar.setObjectName("menubar")
        self.menuoptions = QtWidgets.QMenu(self.menubar)
        self.menuoptions.setObjectName("menuoptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsave_message = QtWidgets.QAction(MainWindow)
        self.actionsave_message.setObjectName("actionsave_message")
        self.actionquit = QtWidgets.QAction(MainWindow)
        self.actionquit.setObjectName("actionquit")
        self.menuoptions.addAction(self.actionsave_message)
        self.menuoptions.addAction(self.actionquit)
        self.menubar.addAction(self.menuoptions.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chatroom")) # If I didn't change at qtdesigner,
        self.pushButton.setText(_translate("MainWindow", "Send"))       # it will need to add a new line
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Text"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Emoji"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Message"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "IP_list"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "other_function"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Check"))
        self.menuoptions.setTitle(_translate("MainWindow", "Options"))
        self.actionsave_message.setText(_translate("MainWindow", "save message"))
        self.actionsave_message.setStatusTip(_translate("MainWindow", "Ctrl+S"))
        self.actionsave_message.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionquit.setText(_translate("MainWindow", "quit"))
        self.actionquit.setStatusTip(_translate("MainWindow", "Ctrl+W"))
        self.actionquit.setShortcut(_translate("MainWindow", "Ctrl+W"))


