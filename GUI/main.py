import pymysql
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mainUI import mainWindow, mainWindowController


if __name__ == "__main__":
    # 创建应用程序
    app = QtWidgets.QApplication(sys.argv)
    # 创建UI控制器
    currentWin = mainWindowController.MainWindowController()
    # 进入消息循环
    sys.exit(app.exec_())
