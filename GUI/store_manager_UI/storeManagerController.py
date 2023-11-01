import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from GUI.store_manager_UI import storeManagerWindow
from GUI.store_manager_UI.addDishController import AddDishController
from GUI.store_manager_UI.addStoreController import AddStoreController


class StoreManagerController(QtWidgets.QMainWindow, storeManagerWindow.Ui_StoreManagerWindow):

    def __init__(self, store_manager_id):
        super(StoreManagerController, self).__init__()
        self.store_manager_id = store_manager_id
        self.currentWin = None
        self.setupUi(self)
        self.show()

        # 绑定按钮事件
        self.addStoreButton.clicked.connect(self.addStore)
        self.deleteStoreButton.clicked.connect(self.deleteStore)
        self.refreshButton.clicked.connect(self.showStoreList)

        # 绑定双击事件
        self.myStoreTableWidget.cellDoubleClicked.connect(self.doubleClicked1)
        self.orderInformationTableWidget.cellDoubleClicked.connect(self.doubleClicked2)

        # 显示商店列表
        self.showStoreList()

        # 显示订单列表
        self.showOrderList()

    def showStoreList(self):
        # 显示商店列表
        # 连接数据库
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        # 创建游标
        cursor = conn.cursor()
        # 执行SQL语句
        sql = "select store.store_name, canteen.canteen_name, store.store_status " \
              "from store, store_manager, canteen " \
              "where store_manager.id = %d and store_manager.store_manager_telephone = store.store_manager_telephone " \
              "and store.canteen_id = canteen.canteen_id" \
              % self.store_manager_id
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
        # 显示结果
        self.myStoreTableWidget.setRowCount(len(result))
        self.myStoreTableWidget.setColumnCount(3)
        self.myStoreTableWidget.setHorizontalHeaderLabels(['食堂名称', '商铺名称', '商铺状态'])
        # 不可修改
        self.myStoreTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i in range(len(result)):
            self.myStoreTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.myStoreTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.myStoreTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))

        cursor.close()
        conn.close()

    def addStore(self):
        # 添加商店
        # 弹出添加商店窗口
        self.currentWin = AddStoreController(self.store_manager_id)

    def deleteStore(self):
        # 删除选中列表中的商店和对应的菜品
        # 获取选中的商店
        selectedItems = self.myStoreTableWidget.selectedItems()
        if len(selectedItems) == 0:
            # 未选中任何商店
            QtWidgets.QMessageBox.warning(self, "提示", "请选中要删除的商店")
            return
        else:
            # 选中了商店
            # 弹出提示框，确认后删除商店，刷新商店列表；取消后不删除商店
            reply = QtWidgets.QMessageBox.question(self, "提示", "确认删除？", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                storeName = selectedItems[1].text()
                # 连接数据库
                conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                                       charset="utf8")
                # 创建游标
                cursor = conn.cursor()
                # 获取store_id
                sql = "select store_id from store where store_name = '%s'" % storeName
                cursor.execute(sql)
                result = cursor.fetchall()
                store_id = result[0][0]
                # 删除菜品
                sql = "delete from dish where store_id = %d" % store_id
                cursor.execute(sql)
                conn.commit()

                # 删除商店
                # 获取商店名称
                sql = "delete from store where store_name = '%s'" % storeName
                cursor.execute(sql)
                conn.commit()
                cursor.close()
                conn.close()
                # 刷新商店列表
                self.showStoreList()
            else:
                return

    def showOrderList(self):
        # 连接数据库
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        # 创建游标
        cursor = conn.cursor()
        # 执行SQL语句
        sql = "select orders.order_id, canteen.canteen_name, store.store_name, orders.normal_user_telephone, " \
              "user_info.location, orders.order_time, orders.order_status " \
              "from orders, canteen, store, store_manager, user_info " \
              "where canteen.canteen_id=orders.order_canteen_id and store.store_id=orders.order_store_id and " \
              "store_manager.store_manager_telephone=store.store_manager_telephone and store_manager.id=%d and " \
              "user_info.id=store_manager.id" \
              % self.store_manager_id

        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
        # 显示结果
        self.orderInformationTableWidget.setRowCount(len(result))
        self.orderInformationTableWidget.setColumnCount(7)
        self.orderInformationTableWidget.setHorizontalHeaderLabels(['订单号', '食堂名称', '商铺名称', '用户电话', '用户位置', '下单时间', '订单状态'])
        # 设置宽度
        self.orderInformationTableWidget.setColumnWidth(5, 200)
        # 只能修改订单状态
        self.orderInformationTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i in range(len(result)):
            self.orderInformationTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.orderInformationTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.orderInformationTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))
            self.orderInformationTableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(result[i][3])))
            self.orderInformationTableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(result[i][4])))
            self.orderInformationTableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(result[i][5])))
            self.orderInformationTableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(result[i][6])))

        cursor.close()
        conn.close()

    def doubleClicked1(self, row, column):
        # 寻找选中store的store_id
        storeName = self.myStoreTableWidget.item(row, 1).text()
        # 连接数据库
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        # 创建游标
        cursor = conn.cursor()
        # 执行SQL语句
        sql = "select store_id from store where store_name = '%s'" % storeName
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
        store_id = result[0][0]
        cursor.close()
        conn.close()
        # 弹出菜品管理界面
        self.currentWin = AddDishController(store_id)

    def doubleClicked2(self, row, column):
        # 双击时间修改订单状态
        # 获取订单号
        order_id = self.orderInformationTableWidget.item(row, 0).text()
        # 获取订单状态
        order_status = self.orderInformationTableWidget.item(row, 6).text()
        # 判断订单状态
        if order_status == "0":
            # 未完成订单
            # 弹出提示框，点击确认后修改订单状态，刷新订单列表；点击取消后不修改订单状态
            reply = QtWidgets.QMessageBox.question(self, "提示", "确认接单？", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                # 修改订单状态
                # 连接数据库
                conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                                       charset="utf8")
                # 创建游标
                cursor = conn.cursor()
                # 执行SQL语句
                sql = "update orders set order_status = 1 where order_id = %d" % int(order_id)
                cursor.execute(sql)
                conn.commit()
                cursor.close()
                conn.close()
                # 刷新订单列表
                self.showOrderList()
            else:
                return
        else:
            # 已接单，不可修改，弹出提示框
            QtWidgets.QMessageBox.information(self, "提示", "此订单已接单")






