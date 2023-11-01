import sys
import pymysql
from PyQt5 import QtCore, QtWidgets, QtGui

from GUI.canteen_manager_UI import addCanteenWindow


class AddCanteenController(QtWidgets.QMainWindow, addCanteenWindow.Ui_AddCanteenWindow):
    def __init__(self, canteen_manager_id):
        self.canteen_manager_id = canteen_manager_id
        super(AddCanteenController, self).__init__()
        self.currentWin = None
        self.setupUi(self)
        self.show()

        # 绑定按钮事件
        self.confirmAddCanteenButton.clicked.connect(self.confirmAddCanteen)
        self.cancelAddCanteenButton.clicked.connect(self.cancelAddCanteen)

    def confirmAddCanteen(self):
        # 确认添加食堂按钮被点击
        # 获取输入框中的内容
        canteenName = self.canteenNameLineEdit.text()
        canteenStartTime = self.canteenStartTimeEdit.time().toString("hh-mm-ss")
        canteenEndTime = self.canteenEndTimeEdit.time().toString("hh-mm-ss")

        # 连接数据库
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        # 创建游标
        cursor = conn.cursor()

        # 获取canteen_manager_telephone
        sql = "select canteen_manager_telephone from canteen_manager where id = %d" % self.canteen_manager_id
        cursor.execute(sql)
        result = cursor.fetchall()
        canteen_manager_telephone = result[0][0]

        # 获取canteen表中最大的canteen_id
        sql = "select canteen_id from canteen order by canteen_id desc limit 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        canteen_id = int(result[0][0]) + 1

        # 插入canteen表中
        sql = "insert into canteen values (%d, %d, '%s', 1, str_to_date('%s', '%%H-%%i-%%s'), str_to_date('%s', '%%H-%%i-%%s'), null)" \
              % (canteen_id, canteen_manager_telephone, canteenName, canteenStartTime, canteenEndTime)
        cursor.execute(sql)
        conn.commit()

        # 关闭窗口，返回食堂
        cursor.close()
        conn.close()
        self.close()

    def cancelAddCanteen(self):
        # 取消添加食堂按钮被点击
        # 关闭窗口，返回食堂管理界面
        self.close()

