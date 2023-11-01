import sys

import pymysql
from PyQt5 import QtCore, QtWidgets, QtGui

from GUI.canteen_manager_UI import canteenManagerController
from GUI.loginUI import loginWindow
from GUI.mainUI import mainWindowController
from GUI.normal_user_UI import normalUserController
from GUI.store_manager_UI import storeManagerController


class LoginWindowController(QtWidgets.QMainWindow, loginWindow.Ui_loginWindow):

    def __init__(self):
        super(LoginWindowController, self).__init__()
        self.currentWin = None
        self.setupUi(self)
        self.show()
        self.loginConfirmButton.clicked.connect(self.login)

    def login(self):
        # 登录按钮被点击
        # 获取输入框中的内容
        loginID = self.loginIDInputLine.text()
        loginPassword = self.loginPasswordInputLine.text()
        # 获取comboBox中的序号
        loginLevel = self.loginLevelSelectComboBox.currentIndex()

        # 连接数据库
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        # 创建游标
        cursor = conn.cursor()
        # 执行SQL语句
        sql = "select * from user_info where id = %d and passwords = %s and user_level = %d" % (int(loginID), loginPassword, loginLevel)
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
        # 判断是否登录成功
        if len(result) == 0:
            # 登录失败
            print("登录失败")
            # 弹出提示框
            QtWidgets.QMessageBox.warning(self, "提示", "登录失败，请检查用户名和密码是否正确")
            self.loginIDInputLine.clear()
            self.loginPasswordInputLine.clear()

        else:
            # 登录成功
            print("登录成功")
            # 弹出提示框
            QtWidgets.QMessageBox.information(self, "提示", "登录成功")
            # 打开对应的用户界面
            if loginLevel == 0:
                # 普通用户
                self.currentWin = normalUserController.NormalUserController(int(loginID))
            elif loginLevel == 1:
                # 商铺管理员
                self.currentWin = storeManagerController.StoreManagerController(int(loginID))
            elif loginLevel == 2:
                # 食堂管理员
                self.currentWin = canteenManagerController.CanteenManagerController(int(loginID))

            # 关闭登录页
            self.close()

        # 关闭数据库连接
        conn.close()
        cursor.close()
