import sys
from PyQt5 import QtCore, QtWidgets, QtGui

from GUI.mainUI import mainWindow
from GUI.loginUI import loginWindow, loginWindowController
from GUI.registerUI import registerWindow, registerWindowController
from GUI.uiController import UIController


class MainWindowController(QtWidgets.QMainWindow, mainWindow.Ui_mainWindow):

    def __init__(self):
        super(MainWindowController, self).__init__()
        self.currentWin = None
        self.setupUi(self)
        self.show()
        self.loginButton.clicked.connect(self.mainWindowLogin)
        self.registerButton.clicked.connect(self.mainWindowRegister)

    def mainWindowLogin(self):
        # 登录按钮被点击切换到登录页
        self.close()
        self.currentWin = loginWindowController.LoginWindowController()

    def mainWindowRegister(self):
        # 注册按钮被点击切换到注册页
        self.close()
        self.currentWin = registerWindowController.RegisterWindowController()
