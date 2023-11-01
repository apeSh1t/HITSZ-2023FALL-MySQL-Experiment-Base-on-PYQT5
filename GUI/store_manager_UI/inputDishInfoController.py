import sys
import pymysql
from PyQt5 import QtCore, QtWidgets, QtGui
from GUI.store_manager_UI import inputDishInfo


class InputDishInfoController(QtWidgets.QMainWindow, inputDishInfo.Ui_InputDishInfoWindow):
    def __init__(self, store_id):
        super(InputDishInfoController, self).__init__()
        self.store_id = store_id
        self.setupUi(self)
        self.show()

        # 绑定按钮事件
        self.confirmButton.clicked.connect(self.confirm)
        self.cancelButton.clicked.connect(self.cancel)

    def confirm(self):
        # 确认按钮被点击
        # 获取输入框中的内容
        dishName = self.dishNameLineEdit.text()
        dishCost = self.dishCostLineEdit.text()
        dishDescription = self.dishDescriptionLineEdit.text()
        dishGradients = self.dishGradientLineEdit.text()

        # 连接数据库
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        # 创建游标
        cursor = conn.cursor()

        # 获取dish_id
        sql = "select dish_id from dish order by dish_id desc limit 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            dish_id = 1
        else:
            dish_id = int(result[0][0]) + 1
        # 插入dish表中
        sql = "insert into dish values (%d, %d, '%s', '%s', %d, '%s')" \
              % (dish_id, self.store_id, dishName, dishDescription, int(dishCost), dishGradients)
        cursor.execute(sql)
        conn.commit()

        # 关闭数据库连接
        cursor.close()
        conn.close()

        # 关闭当前窗口
        self.close()

    def cancel(self):
        self.close()

