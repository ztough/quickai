import sys
from PySide6.QtWidgets import QApplication, QWidget, QMenu, QSystemTrayIcon,QInputDialog, QDialog, QVBoxLayout, QLabel, QLineEdit, QKeySequenceEdit, QPushButton,QMessageBox
from PySide6.QtGui import QIcon, QAction,QCloseEvent, QStandardItemModel, QStandardItem,QDesktopServices
from ui_form import Ui_main
from PySide6.QtCore import QSettings,Qt,QModelIndex,QDateTime, QDir, QPoint, QUrl,QFileInfo
from action import action
from web import web
import json
from pynput.keyboard import Controller, Key
from pynput import mouse
import time
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
settings=QSettings("QuickAi", "Settings")
class CustomInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QIcon('img/logo.png'))
        self.setWindowTitle('输入提示词和快捷键')
        self.resize(300, 150)
        layout = QVBoxLayout()

        # 输入文本标签和输入框
        self.label_text = QLabel('输入提示词({text}为引用的文本): ')
        self.line_edit = QLineEdit()
        layout.addWidget(self.label_text)
        layout.addWidget(self.line_edit)

        # 输入快捷键标签和输入框
        self.label_key_sequence = QLabel('输入快捷键:')
        self.key_sequence_edit = QKeySequenceEdit()
        self.key_sequence_edit.setMaximumSequenceLength(1)
        layout.addWidget(self.label_key_sequence)
        layout.addWidget(self.key_sequence_edit)

        # 确定和取消按钮
        self.button_box = QPushButton('确定')
        self.button_box.clicked.connect(self.accept)
        layout.addWidget(self.button_box)

        self.setLayout(layout)

    def get_inputs(self):
        return self.line_edit.text(), self.key_sequence_edit.keySequence().toString()
class main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("img/logo.png"))
        self.ui.tabWidget.setCurrentIndex(0)
        self.setMaximumSize(self.size())
        self.setMinimumSize(self.size())
        self.settings = QSettings("QuickAi", "Settings")
        self.a=action()
        self.a.menu()
        self.w=web()
        self.network_manager = QNetworkAccessManager(self)
        self.ui.comboBox.setCurrentIndex(self.settings.value("model",0))
        self.ui.checkBox.setChecked(self.settings.value("popup",0))
        self.ui.checkBox_2.setChecked(self.settings.value("popups",0))
        self.ui.checkBox_3.setChecked(self.settings.value("tray",0))
        self.ui.checkBox_4.setChecked(self.settings.value("start",0))
        self.trayIcon = QSystemTrayIcon(QIcon("img/logo.png"), self)
        self.trayMenu = QMenu()

        # 创建动作
        self.actionShow = QAction("显示", self)
        self.actionExit = QAction("退出", self)

        # 添加动作到菜单
        self.trayMenu.addAction(self.actionShow)
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(self.actionExit)

        # 设置托盘图标的上下文菜单
        self.trayIcon.setContextMenu(self.trayMenu)

        # 连接动作的触发信号
        self.actionShow.triggered.connect(self.showNormal)
        self.actionShow.triggered.connect(self.activateWindow)
        self.actionExit.triggered.connect(QApplication.instance().quit)

        # 连接托盘图标的双击事件
        self.trayIcon.activated.connect(self.handleTrayIconActivated)
        self.createContextMenu()
        self.createContextMenus()
        # 显示托盘图标
        self.trayIcon.show()
        self.list_model = QStandardItemModel()
        self.ui.listView.setModel(self.list_model)
        item_list = self.settings.value("category","[]")
        for text in json.loads(item_list):
            item = QStandardItem(text)
            self.list_model.appendRow(item)
        self.table_model=QStandardItemModel(0, 2)
        self.table_model.setHorizontalHeaderLabels(['提示词', '快捷键'])
        self.ui.tableView.setModel(self.table_model)
        self.ui.tableView.setColumnWidth(0, 100)
        self.ui.tableView.setColumnWidth(1, 80)
        self.list_model.dataChanged.connect(self.save)
        self.table_model.dataChanged.connect(self.save)
        if self.list_model.rowCount()>0:
            self.ui.listView.setCurrentIndex(self.list_model.index(0,0))
            self.category_click(self.list_model.index (0,0))
        self.mouse_listener = mouse.Listener(on_click=self.on_click, on_move=self.on_move)
        self.mouse_listener.start()
        self.click_time = 0
        self.long_press_threshold = 0.15
        self.move_threshold = 20
        self.initial_pos = None
        self.current_pos = None
        self.ui.label_2.setVisible(False)
        self.updateCheck()
    def ztough(self):
        url = QUrl("https://ztough.cn")
        QDesktopServices.openUrl(url)
    def tutorial(self):
        url = QUrl("https://tkjpydwgii.feishu.cn/wiki/M5Niw4kp8iJMJZkPZLTcZNNonid?from=from_copylink")
        QDesktopServices.openUrl(url)
    def renew(self):
        url = QUrl("https://ztough.cn/buy/quickai")
        QDesktopServices.openUrl(url)
    def updateCheck(self):
        url = QUrl("https://ztough-1308253351.cos.ap-nanjing.myqcloud.com/quickai.txt")
        request = QNetworkRequest(url)
        reply = self.network_manager.get(request)
        reply.finished.connect(lambda: self.handle_reply(reply))

    def handle_reply(self, reply):
        if reply.error() == QNetworkReply.NoError:
            update = reply.readAll().data().decode('utf-8').strip()
            file_path = QDir(QApplication.applicationDirPath()).filePath("QuickAi.exe")
            file_info = QFileInfo(file_path)
            new_version = QDateTime.fromString(update, "yyyy-MM-dd HH:mm:ss")
            now_version = file_info.lastModified()
            if new_version > now_version:
                self.ui.label_2.setVisible(True)
        reply.deleteLater()

    def on_click(self, x, y, button, pressed):
        if self.ui.checkBox_2.isChecked() and button == mouse.Button.left:

            if pressed:
                self.click_time = time.time()
                self.initial_pos = (x, y)
                self.current_pos = (x, y)
            else:
                duration = time.time() - self.click_time
                if duration >= self.long_press_threshold and self.distance_moved(self.initial_pos, self.current_pos) >= self.move_threshold:
                    self.show_hover_window(x, y)
                elif not self.a.rect().contains(self.a.mapFromGlobal(QPoint(x,y))):
                    self.a.hide()

    def on_move(self, x, y):
        if self.initial_pos:
            self.current_pos = (x, y)

    def distance_moved(self, start, end):
        return ((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5
    def show_hover_window(self, x, y):
        self.a.show()
        self.a.move(QPoint(x+20, y+20))
    def simulate_ctrl_c(self):
        keyboard = Controller()
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
    def ai(self):
        self.w.open_ai(self.ui.comboBox.currentIndex())
    def category_click(self,index:QModelIndex):
        category=self.list_model.itemFromIndex(index).text()
        data = json.loads(self.settings.value(category,"[]"))

        self.table_model.clear()
        self.table_model.setHorizontalHeaderLabels(['提示词', '快捷键'])
        '''
        if len(data)==0:
            if category=="提问":
                data=[['能解释一下这段话的意思吗？{text}',''],['能给出{text}的定义吗？',''],['能给出{text}的用途是什么？',''],['可以举个{text}的例子吗？',''],['完成这项任务的步骤有哪些？{text}',''],['{text}的优缺点是什么？',''],['{text}的工作原理是什么？',''],['你能拓展一下{text}相关的资料吗？',''],['你能拓展一下{text}相关的资料吗？',''],['{text}的历史背景是什么？','']]
            if category=="追问":
                data=[['你能进一步说明一下这个观点吗？',''],['还有哪些信息需要补充？',''],['能用通俗易懂的大白话再次解释下吗？','']]
        '''
        for row_data in data:
            row_items = [QStandardItem(item) for item in row_data]
            self.table_model.appendRow(row_items)
    def closeEvent(self, event: QCloseEvent):
        event.ignore()  # 忽略关闭事件，即不直接关闭窗口
        self.hide()     # 隐藏窗口而不是关闭
    def handleTrayIconActivated(self, reason):
        # 处理托盘图标的激活事件
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.showNormal()
            self.activateWindow()
    def model(self,index):
        self.settings.setValue("model",index)
    def popup(self,index):
        self.settings.setValue("popup",index)
        if index==2:
            self.a.show()
        else:
            self.a.hide()
    def popups(self,index):
        self.settings.setValue("popups",index)
        if self.ui.checkBox.isChecked():
            self.a.show()
    def tray(self,index):
        self.settings.setValue("tray",index)
    def start(self,index):
        self.settings.setValue("start",index)
        if index:
            # 添加启动项到注册表
            settings = QSettings("HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", QSettings.NativeFormat)
            settings.setValue("QuickAi", QApplication.applicationFilePath().replace("/", "\\"))

        else:
            # 移除启动项
            settings = QSettings("HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", QSettings.NativeFormat)
            settings.remove("QuickAi")
    def createContextMenu(self):
        # 创建右键菜单
        self.contextMenu = QMenu(self.ui.listView)

        # 添加动作到右键菜单
        addAction = QAction("添加", self)
        deleteAction = QAction("删除", self)

        self.contextMenu.addAction(addAction)
        self.contextMenu.addAction(deleteAction)

        # 连接动作的触发信号到槽函数
        addAction.triggered.connect(self.addActionClicked)
        deleteAction.triggered.connect(self.deleteActionClicked)

        # 设置列表视图的上下文菜单策略
        self.ui.listView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.listView.customContextMenuRequested.connect(self.showContextMenu)
    def createContextMenus(self):
        # 创建右键菜单
        self.contextMenus = QMenu(self.ui.tableView)

        # 添加动作到右键菜单
        addAction = QAction("添加", self)
        deleteAction = QAction("删除", self)

        self.contextMenus.addAction(addAction)
        self.contextMenus.addAction(deleteAction)

        # 连接动作的触发信号到槽函数
        addAction.triggered.connect(self.addActionClickeds)
        deleteAction.triggered.connect(self.deleteActionClickeds)

        # 设置列表视图的上下文菜单策略
        self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.showContextMenus)
    def showContextMenu(self, position):
        # 显示右键菜单
        self.contextMenu.exec(self.ui.listView.mapToGlobal(position))
    def showContextMenus(self, position):
        # 显示右键菜单
        self.contextMenus.exec(self.ui.tableView.mapToGlobal(position))
    def addActionClicked(self):
        # 添加条目
        text, ok = QInputDialog.getText(self, "添加分类", "输入分类名")
        if ok and text:
            item = QStandardItem(text)
            self.list_model.appendRow(item)
            self.save()

    def deleteActionClicked(self):
        # 删除选中的条目
        indexes = self.ui.listView.selectedIndexes()
        if indexes:
            index = indexes[0]
            self.list_model.removeRow(index.row())
            self.ui.listView.clearSelection()
            self.save()

    def addActionClickeds(self):
        selected_indexes = self.ui.listView.selectedIndexes()
        if selected_indexes:
            dialog = CustomInputDialog()
            if dialog.exec():
                text, key_sequence = dialog.get_inputs()
                row=[]
                row.append(QStandardItem(text))
                row.append(QStandardItem(key_sequence))
                self.table_model.appendRow(row)
                self.save()

        else:
            QMessageBox.critical(self, '错误', '请先选中左侧的项', QMessageBox.Ok)

    def save(self):
        item_list = [self.list_model.item(row).text() for row in range(self.list_model.rowCount())]
        self.settings.setValue("category",json.dumps(item_list,ensure_ascii=False))
        rows = self.table_model.rowCount()
        cols = self.table_model.columnCount()
        data=[]
        for row in range(rows):
            row_data = []
            for col in range(cols):
                index = self.table_model.index(row, col)
                item = self.table_model.data(index)
                row_data.append(item)
            data.append(row_data)
        selected_indexes = self.ui.listView.selectedIndexes()
        if selected_indexes:
            self.settings.setValue(self.list_model.itemFromIndex(selected_indexes[0]).text(),json.dumps(data, ensure_ascii=False))
        self.a.menu()
    def deleteActionClickeds(self):
        # 删除选中的条目
        indexes = self.ui.tableView.selectedIndexes()
        if indexes:
            index = indexes[0]
            self.table_model.removeRow(index.row())
            self.save()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = main()
    if settings.value("tray"):
        widget.hide()
    else:
        widget.show()
    sys.exit(app.exec())
