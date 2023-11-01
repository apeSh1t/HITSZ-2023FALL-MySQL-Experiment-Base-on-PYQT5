import sys

import pymysql
from PyQt5 import QtCore, QtWidgets, QtGui

from GUI.loginUI import loginWindowController
from GUI.registerUI import registerWindow
from GUI.mainUI import mainWindowController


class RegisterWindowController(QtWidgets.QMainWindow, registerWindow.Ui_registerWindow):
    def __init__(self):
        super(RegisterWindowController, self).__init__()
        self.currentWin = None
        self.setupUi(self)
        self.show()
        self.registerConfirmButton.clicked.connect(self.register)

    def register(self):
        # 注册按钮被点击
        # 获取输入框中的内容
        registerID = self.registerIDInputLine.text()
        registerPassword = self.registerPasswordInputLine.text()
        registerName = self.registerNicknameInputLine.text()
        registerAddress = self.registerAddressInputLine.text()
        registerTelephone = self.registerTelephoneInputLine.text()

        # 获取comboBox中的序号
        registerLevel = self.registerLevelSelectComboBox.currentIndex()

        if registerID and registerPassword:
            conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                                   charset="utf8")
            # 创建游标
            cursor = conn.cursor()

            # 查看是否有重复的ID
            sql = "select * from user_info where id = %d" % int(registerID)
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result) != 0:
                # 有重复的ID
                # 弹出提示框
                print(result)
                QtWidgets.QMessageBox.warning(self, "提示", "注册失败，该ID已被注册，请更换ID")
                self.registerIDInputLine.clear()
                self.registerPasswordInputLine.clear()
                self.registerNicknameInputLine.clear()
                self.registerAddressInputLine.clear()
                self.registerIDInputLine.clear()
                self.registerTelephoneInputLine.clear()

            else:
                # 插入用户信息
                sql = "insert into user_info (id, passwords, nickname, location, user_level) values (%d, '%s', '%s', '%s', '%d')"\
                      % (int(registerID), registerPassword, registerName, registerAddress, registerLevel)

                cursor.execute(sql)

                if registerLevel == 0:
                    info = "normal_user"
                elif registerLevel == 1:
                    info = "store_manager"
                else:
                    info = "canteen_manager"

                sql = "insert into %s (id, %s_telephone) values (%d, %d)" \
                      % (info, info, int(registerID), int(registerTelephone))
                cursor.execute(sql)

                # 提交事务
                conn.commit()
                # 关闭数据库连接
                conn.close()
                cursor.close()
                # 弹出提示框
                QtWidgets.QMessageBox.information(self, "提示", "注册成功")
                # 关闭注册页
                self.close()
                # 打开主页
                self.currentWin = mainWindowController.MainWindowController()

        else:
            QtWidgets.QMessageBox.warning(self, "提示", "注册失败，请检查用户名和密码是否为空")
