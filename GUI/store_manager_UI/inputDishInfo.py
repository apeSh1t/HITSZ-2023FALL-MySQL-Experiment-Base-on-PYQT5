# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputDishInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InputDishInfoWindow(object):
    def setupUi(self, InputDishInfoWindow):
        InputDishInfoWindow.setObjectName("InputDishInfoWindow")
        InputDishInfoWindow.resize(1092, 785)
        self.centralwidget = QtWidgets.QWidget(InputDishInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 60, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 220, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 310, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 400, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 500, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.dishNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dishNameLineEdit.setGeometry(QtCore.QRect(380, 230, 291, 41))
        self.dishNameLineEdit.setObjectName("dishNameLineEdit")
        self.dishCostLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dishCostLineEdit.setGeometry(QtCore.QRect(380, 320, 291, 41))
        self.dishCostLineEdit.setObjectName("dishCostLineEdit")
        self.dishDescriptionLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dishDescriptionLineEdit.setGeometry(QtCore.QRect(380, 410, 291, 41))
        self.dishDescriptionLineEdit.setObjectName("dishDescriptionLineEdit")
        self.dishGradientLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dishGradientLineEdit.setGeometry(QtCore.QRect(380, 500, 291, 41))
        self.dishGradientLineEdit.setObjectName("dishGradientLineEdit")
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(320, 620, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(520, 620, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        InputDishInfoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InputDishInfoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 30))
        self.menubar.setObjectName("menubar")
        InputDishInfoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InputDishInfoWindow)
        self.statusbar.setObjectName("statusbar")
        InputDishInfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InputDishInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(InputDishInfoWindow)

    def retranslateUi(self, InputDishInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        InputDishInfoWindow.setWindowTitle(_translate("InputDishInfoWindow", "MainWindow"))
        self.label.setText(_translate("InputDishInfoWindow", "新增菜品🍖"))
        self.label_2.setText(_translate("InputDishInfoWindow", "菜品名称"))
        self.label_3.setText(_translate("InputDishInfoWindow", "菜品单价"))
        self.label_4.setText(_translate("InputDishInfoWindow", "菜品描述"))
        self.label_5.setText(_translate("InputDishInfoWindow", "菜品原料"))
        self.confirmButton.setText(_translate("InputDishInfoWindow", "确认"))
        self.cancelButton.setText(_translate("InputDishInfoWindow", "取消"))