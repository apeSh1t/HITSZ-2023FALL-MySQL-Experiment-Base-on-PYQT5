import sys
import pymysql
from PyQt5 import QtCore, QtWidgets, QtGui

from GUI.store_manager_UI import addStoreWindow


class AddStoreController(QtWidgets.QMainWindow, addStoreWindow.Ui_AddStoreWindow):

    def __init__(self, store_manager_id):
        super(AddStoreController, self).__init__()
        self.store_manager_id = store_manager_id
        self.currentWin = None
        self.setupUi(self)
        self.show()

        # 绑定按钮事件
        self.confirmAddStoreButton.clicked.connect(self.confirmAddStore)

    def confirmAddStore(self):
        # 确认添加商铺按钮被点击
        # 获取输入框中的内容
        canteenName = self.canteenNameLineEdit.text()
        storeName = self.storeNameLineEdit.text()
        storeStartTime = self.storeStartTimeEdit.time().toString("hh-mm-ss")
        storeEndTime = self.storeEndTimeEdit.time().toString("hh-mm-ss")

        # 连接数据库
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        # 创建游标
        cursor = conn.cursor()

        # 获取canteen_id
        sql = "select canteen_id from canteen where canteen_name = '%s'" % canteenName
        cursor.execute(sql)
        result = cursor.fetchall()
        canteen_id = result[0][0]

        # 获取store_manager_telephone
        sql = "select store_manager_telephone from store_manager where id = %d" % self.store_manager_id
        cursor.execute(sql)
        result = cursor.fetchall()
        store_manager_telephone = result[0][0]

        # 获取store表中最大的store_id
        sql = "select store_id from store order by store_id desc limit 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            store_id = 1
        else:
            store_id = int(result[0][0]) + 1

        # 插入store表中
        sql = "insert into store values (%d, %d, %d, 1, '%s', str_to_date('%s', '%%H-%%i-%%s'), str_to_date('%s', '%%H-%%i-%%s'), null)" \
              % (store_id, canteen_id, store_manager_telephone, storeName, storeStartTime, storeEndTime)
        cursor.execute(sql)
        conn.commit()

        # 关闭窗口，返回商铺管理界面
        cursor.close()
        conn.close()
        self.close()

    def cancelAddStore(self):
        self.close()


