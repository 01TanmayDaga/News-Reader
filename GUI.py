# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, MainWindow):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 511)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 0, 720, 51))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.q_2 = QtWidgets.QLineEdit(self.main_page)
        self.q_2.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.q_2.setFont(font)
        self.q_2.setText("")
        self.q_2.setMaxLength(20)
        self.q_2.setReadOnly(False)
        self.q_2.setObjectName("q_2")
        self.Option = QtWidgets.QComboBox(self.main_page)
        self.Option.setGeometry(QtCore.QRect(210, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Option.setFont(font)
        self.Option.setEditable(False)
        self.Option.setCurrentText("")
        self.Option.setObjectName("Option")
        self.Cat = QtWidgets.QComboBox(self.main_page)
        self.Cat.setGeometry(QtCore.QRect(410, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cat.setFont(font)
        self.Cat.setEditable(False)
        self.Cat.setCurrentText("")
        self.Cat.setObjectName("Cat")
        self.count = QtWidgets.QComboBox(self.main_page)
        self.count.setGeometry(QtCore.QRect(570, 10, 131, 31))
        self.count.setEditable(False)
        self.count.setObjectName("count")
        self.stackedWidget_2.addWidget(self.main_page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.Option_2 = QtWidgets.QComboBox(self.page_2)
        self.Option_2.setGeometry(QtCore.QRect(210, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Option_2.setFont(font)
        self.Option_2.setEditable(False)
        self.Option_2.setCurrentText("")
        self.Option_2.setObjectName("Option_2")
        self.Language = QtWidgets.QComboBox(self.page_2)
        self.Language.setGeometry(QtCore.QRect(570, 10, 131, 31))
        self.Language.setEditable(False)
        self.Language.setObjectName("Language")
        self.Sort_by = QtWidgets.QComboBox(self.page_2)
        self.Sort_by.setGeometry(QtCore.QRect(410, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sort_by.setFont(font)
        self.Sort_by.setEditable(False)
        self.Sort_by.setCurrentText("")
        self.Sort_by.setObjectName("Sort_by")
        self.q_3 = QtWidgets.QLineEdit(self.page_2)
        self.q_3.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.q_3.setFont(font)
        self.q_3.setText("")
        self.q_3.setMaxLength(20)
        self.q_3.setReadOnly(False)
        self.q_3.setObjectName("q_3")
        self.stackedWidget_2.addWidget(self.page_2)
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 52, 720, 461))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 2, 720, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
