import random
import sys

import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from GUI.normal_user_UI import normalUserWindow
from GUI.normal_user_UI.numberSelectController import NumberSelectController


class NormalUserController(QtWidgets.QMainWindow, normalUserWindow.Ui_NormalUserWindow):
    order_id = random.randint(100000, 999999)
    store_id = 0
    canteen_id = 0
    normal_user_telephone = 0

    def __init__(self, user_id):
        super(NormalUserController, self).__init__()
        self.currentWin1 = None
        self.currentWin2 = None
        self.user_id = user_id
        self.setupUi(self)
        # label显示用户信息
        self.showText()
        # 加载用户头像
        self.normalUserLoadPhotoButton.clicked.connect(self.loadPhoto)

        # 绑定双击事件
        self.normalUserTableWidget.cellDoubleClicked.connect(self.doubleClicked)

        # 绑定按钮事件
        self.normalUserConfirmButton.clicked.connect(self.normalUserConfirm)

        self.show()

    def showText(self):
        # 查找用户昵称
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        cursor = conn.cursor()
        sql = "select nickname, passwords, location, profile_photo from user_info where id = %d" % self.user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        self.normalUserNameLabel.setText(result[0][0])
        self.normalUserIDLabel.setText(str(self.user_id))
        self.normalUserPasswordLabel.setText(result[0][1])
        self.normalUserAddressLabel.setText(result[0][2])
        self.normalUserPhotoLabel.setPixmap(QtGui.QPixmap(result[0][3]))

        sql = "select normal_user_telephone from normal_user where id = %d" % self.user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        self.normal_user_telephone = result[0][0]
        self.normalUserTelephoneLabel.setText(str(self.normal_user_telephone))

        # 表格显示菜单信息
        sql = "select * from view_dish_list order by canteen_name, store_name"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.normalUserTableWidget.setRowCount(len(result))
        self.normalUserTableWidget.setColumnCount(7)
        self.normalUserTableWidget.setHorizontalHeaderLabels(["食堂照片", "食堂名称", "商铺名称", "菜品名称", "菜品价格",  "菜品原料", "菜品描述"])
        for i in range(len(result)):
            for j in range(7):
                newItem = QtWidgets.QTableWidgetItem(str(result[i][j]))
                self.normalUserTableWidget.setItem(i, j, newItem)

        conn.close()

    def loadPhoto(self):
        # 加载用户头像
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.normalUserPhotoLabel.width(), self.normalUserPhotoLabel.height())
        self.normalUserPhotoLabel.setPixmap(jpg)

        # img = open(imgName, "rb").read()
        # # 将图片保存到数据库
        # conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
        #                        charset="utf8")
        # cursor = conn.cursor()
        # sql = "update user_info set profile_photo = %s where id = %d;" % (pymysql.Binary(img), self.user_id)
        # cursor.execute(sql)
        #
        # conn.commit()
        # conn.close()

    def doubleClicked(self, row, col):
        # 查找菜品ID
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        cursor = conn.cursor()
        sql = "select dish_id from dish where dish_name = '%s'" % self.normalUserTableWidget.item(row, 3).text()
        cursor.execute(sql)
        result = cursor.fetchall()
        dish_id = result[0][0]

        # 弹出数量选择框
        self.currentWin2 = NumberSelectController(order_id=self.order_id, dish_id=int(dish_id))

        # 查找商铺ID
        sql = "select store_id from dish where dish_name = '%s'" % self.normalUserTableWidget.item(row, 3).text()
        cursor.execute(sql)
        result = cursor.fetchall()
        self.store_id = result[0][0]

        # 查找食堂ID
        sql = "select canteen_id from store where store_id = %d" % self.store_id
        cursor.execute(sql)
        result = cursor.fetchall()
        self.canteen_id = result[0][0]

        cursor.close()
        conn.close()

    def normalUserConfirm(self):
        total_cost = 0
        # 调用calculate_cost存储过程计算订单总价
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        cursor = conn.cursor()
        sql = "call calculate_cost('%d')" % self.order_id
        cursor.execute(sql)
        total_cost = cursor.fetchall()[0][0]
        print("本次金额为：" + str(total_cost))
        conn.commit()

        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        cursor = conn.cursor()

        # 跳出提示框，显示本次消费金额和菜品信息
        sql = "select dish_name, dish_num " \
              "from order_dish, dish " \
              "where order_dish.order_id = %d and dish.dish_id = order_dish.dish_id" % self.order_id
        cursor.execute(sql)
        result = cursor.fetchall()
        info = "本次消费金额为：" + str(total_cost) + " 元" + "\n" + "菜名\t\t\t" + "数量\n"
        for i in range(len(result)):
            info += str(result[i][0]) + "\t\t\t" + str(result[i][1]) + "\n"

        QtWidgets.QMessageBox.information(self, "请支付", info)

        # 向order表中插入记录
        sql = "insert into orders values (%d, %d, %d, %f, %d, %d, timestamp(now()), 0)" \
              % (self.order_id, self.normal_user_telephone, self.store_id, total_cost, self.canteen_id, self.store_id)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
