import sys
import pymysql
from PyQt5 import QtCore, QtWidgets, QtGui
from GUI.canteen_manager_UI import canteenManagerWindow
from GUI.canteen_manager_UI.addCanteenController import AddCanteenController


class CanteenManagerController(QtWidgets.QMainWindow, canteenManagerWindow.Ui_CanteenManagerWindow):
    def __init__(self, canteen_manager_id):
        self.canteen_manager_id = canteen_manager_id
        super(CanteenManagerController, self).__init__()
        self.currentWin = None
        self.setupUi(self)
        self.show()
        # 绑定按钮事件
        self.addCanteenButton.clicked.connect(self.addCanteen)
        self.deleteCanteenButton.clicked.connect(self.deleteCanteen)
        self.canteenRefreshButton.clicked.connect(self.showCanteenList)
        self.showCanteenList()

    def showCanteenList(self):
        # 显示食堂列表
        # 连接数据库
        conn = pymysql.connect(host="localhost", user="root", password="yu@20030625", database="canteen",
                               charset="utf8")
        # 创建游标
        cursor = conn.cursor()
        # 执行SQL语句
        sql = "select canteen_name, canteen_status, canteen_open_time, canteen_close_time " \
              "from canteen, canteen_manager " \
              "where canteen.canteen_manager_telephone = canteen_manager.canteen_manager_telephone and id = %d" \
              % self.canteen_manager_id
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
        # 显示结果
        self.myCanteenTableWidget.setRowCount(len(result))
        self.myCanteenTableWidget.setColumnCount(4)
        self.myCanteenTableWidget.setHorizontalHeaderLabels(['食堂名称', '食堂状态', '食堂开门时间', '食堂停业时间'])
        # 不可修改
        self.myCanteenTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i in range(len(result)):
            self.myCanteenTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.myCanteenTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.myCanteenTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))
            self.myCanteenTableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(result[i][3])))
        cursor.close()
        conn.close()

    def addCanteen(self):
        # 添加食堂按钮被点击
        self.currentWin = AddCanteenController(self.canteen_manager_id)
        self.currentWin.show()

    def deleteCanteen(self):
        # 删除食堂按钮被点击
        # 获取选中的行
        selectedItems = self.myCanteenTableWidget.selectedItems()
        if len(selectedItems) == 0:
            QtWidgets.QMessageBox.warning(self, "警告", "请选中要删除的食堂", QtWidgets.QMessageBox.Yes)
            return
        else:
            reply = QtWidgets.QMessageBox.question(self, "提示", "确认删除？", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.No:
                return
            else:
                row = selectedItems[0].row()
                # 获取选中行的食堂名称
                canteenName = self.myCanteenTableWidget.item(row, 0).text()
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

                sql = "set foreign_key_checks = 0"
                cursor.execute(sql)
                conn.commit()

                # 删除canteen表，store表中的记录
                sql = "delete from canteen where canteen_id = %d" % canteen_id
                cursor.execute(sql)
                conn.commit()

                sql = "delete from store where canteen_id = %d" % canteen_id
                cursor.execute(sql)
                conn.commit()
                # 关闭窗口，返回食堂管理界面
                cursor.close()
                conn.close()

                # 刷新食堂列表
                self.showCanteenList()
