import sys
from PyQt5 import QtCore, QtWidgets, QtCore

from GUI.registerUI import registerWindow
from GUI.loginUI import loginWindow
from GUI.mainUI import mainWindow


class UIController:
    def __init__(self):
        self.main = mainWindow.Ui_mainWindow()
        self.login = loginWindow.Ui_loginWindow()
        self.register = registerWindow.Ui_registerWindow()


