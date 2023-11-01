import sys
import pymysql
from PyQt5 import QtCore, QtWidgets, QtGui

from GUI.store_manager_UI import addDishWindow
from GUI.store_manager_UI.inputDishInfoController import InputDishInfoController


class AddDishController(QtWidgets.QMainWindow, addDishWindow.Ui_AddDishWindow):
    def __init__(self, store_id):
        self.currentWin = None
        self.store_id = store_id
        super(AddDishController, self).__init__()
        self.setupUi(self)
        self.show()

        # 绑定按钮事件
        self.dishAddButton.clicked.connect(self.dishAdd)
        self.dishDeleteButton.clicked.connect(self.dishDelete)
        self.dishRefreshButton.clicked.connect(self.dishListShow)

        self.dishListShow()

    def dishListShow(self):
        # 显示菜品列表
        # 连接数据库
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        # 创建游标
        cursor = conn.cursor()
        # 执行SQL语句
        sql = "select dish_name, dish_cost, dish_description, dish_gradients " \
              "from dish " \
              "where store_id = %d" % self.store_id
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
        # 显示结果
        self.dishTableWidget.setRowCount(len(result))
        self.dishTableWidget.setColumnCount(4)
        self.dishTableWidget.setHorizontalHeaderLabels(['菜品名称', '菜品价格', '菜品描述', '菜品原料'])
        # 不可修改
        self.dishTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i in range(len(result)):
            self.dishTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.dishTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.dishTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))
            self.dishTableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(result[i][3])))
        cursor.close()
        conn.close()

    def dishAdd(self):
        self.currentWin = InputDishInfoController(self.store_id)

    def dishDelete(self):
        # 删除选中的菜品
        # 获取选中的行
        selectedItems = self.dishTableWidget.selectedItems()
        if len(selectedItems) == 0:
            QtWidgets.QMessageBox.warning(self, "警告", "请选中要删除的菜品", QtWidgets.QMessageBox.Yes)
            return
        else:
            # 获取选中的行号
            selectedRows = set()
            for item in selectedItems:
                selectedRows.add(item.row())
            # 获取选中行的菜品名称
            dishNames = []
            for row in selectedRows:
                dishNames.append(self.dishTableWidget.item(row, 0).text())
            # 连接数据库
            conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                                   charset="utf8")
            # 创建游标
            cursor = conn.cursor()
            # 执行SQL语句
            for dishName in dishNames:
                sql = "delete from dish where dish_name = '%s'" % dishName
                cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            # 刷新菜品列表
            self.dishListShow()
