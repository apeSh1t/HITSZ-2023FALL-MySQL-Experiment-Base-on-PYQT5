import sys
import random

import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

from GUI.normal_user_UI import numberSelectWindow


class NumberSelectController(QtWidgets.QMainWindow, numberSelectWindow.Ui_NumberSelectWindow):

    def __init__(self, order_id, dish_id):
        self.order_dish_index = random.randint(100000, 999999)
        self.order_id = order_id
        self.dish_id = dish_id
        super(NumberSelectController, self).__init__()
        self.currentWin = None
        self.setupUi(self)
        self.numberSelectConfirmButton.clicked.connect(self.numberSelectConfirm)
        self.numberSelectCancelButton.clicked.connect(self.numberSelectCancel)
        self.show()

    def numberSelectConfirm(self):
        # 获取数量
        number = self.numberSelectSpinBox.value()
        # 插入表order_dish
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        cursor = conn.cursor()
        sql = "set foreign_key_checks=0"
        cursor.execute(sql)
        conn.commit()

        # 判断是否一个订单内有相同的菜品
        sql = "select * from order_dish where order_id = %d and dish_id = %d" % (self.order_id, self.dish_id)
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) != 0:
            # 有相同的菜品,更新数量
            sql = "update order_dish set dish_num = %d where order_id = %d and dish_id = %d" \
                  % (number, self.order_id, self.dish_id)
            cursor.execute(sql)
            conn.commit()
            conn.close()
            self.close()

        else:
            # 没有相同的菜品,插入新的记录
            sql = "insert into order_dish (order_dish_index, order_id, dish_id, dish_num) values (%d, %d, %d, %d)" \
                  % (self.order_dish_index, self.order_id, self.dish_id, number)
            print(sql)
            cursor.execute(sql)
            conn.commit()
            conn.close()
            self.close()

    def numberSelectCancel(self):
        self.close()
