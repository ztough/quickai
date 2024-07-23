# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QListView, QPushButton, QSizePolicy, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(264, 241)
        self.tabWidget = QTabWidget(main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 271, 251))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 261, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6BC6FF, stop:1 #0077FF);\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    border-color: #005D9F;\n"
"    color: white;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #7EDFFF, stop:1 #0088FF);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #005D9F;\n"
"    border-color: #003366;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_11 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #7CFC00, stop:1 #32CD32);\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    border-color: #006400;\n"
"    color: white;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ADFF2F, stop:1 #7FFF00);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #006400;\n"
"    border-color: #003300;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_11)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FF6B6B, stop:1 #FF0077);\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    border-color: #9F005D;\n"
"    color: white;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FF7E7E, stop:1 #FF0088);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #9F005D;\n"
"    border-color: #660033;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_7 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFA500, stop:1 #FF7F00);\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    border-color: #8B4500;\n"
"    color: white;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFBF00, stop:1 #FF8800);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8B4500;\n"
"    border-color: #663300;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 200, 201, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayoutWidget = QWidget(self.tab_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 80, 261, 131))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.horizontalLayoutWidget)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout.addWidget(self.listView)

        self.line = QFrame(self.horizontalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.tableView = QTableView(self.horizontalLayoutWidget)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout.addWidget(self.tableView)

        self.horizontalLayout.setStretch(0, 1)
        self.gridLayoutWidget = QWidget(self.tab_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 30, 261, 51))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_2 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 1, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.checkBox_4, 1, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 261, 31))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.gridLayoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(main)
        self.comboBox.activated.connect(main.model)
        self.checkBox.stateChanged.connect(main.popup)
        self.checkBox_2.stateChanged.connect(main.popups)
        self.checkBox_3.stateChanged.connect(main.tray)
        self.checkBox_4.stateChanged.connect(main.start)
        self.listView.clicked.connect(main.category_click)
        self.pushButton.clicked.connect(main.ai)
        self.pushButton_6.clicked.connect(main.ai)
        self.pushButton_11.clicked.connect(main.ztough)
        self.pushButton_4.clicked.connect(main.tutorial)
        self.pushButton_7.clicked.connect(main.renew)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"QuickAi\u5feb\u95eeAi", None))
        self.pushButton_6.setText(QCoreApplication.translate("main", u"\u6253\u5f00Ai\u5927\u6a21\u578b\u5b98\u7f51", None))
        self.pushButton_11.setText(QCoreApplication.translate("main", u"\u6253\u5f00\u5b98\u7f51", None))
        self.pushButton_4.setText(QCoreApplication.translate("main", u"\u6253\u5f00\u6559\u7a0b", None))
        self.pushButton_7.setText(QCoreApplication.translate("main", u"\u7eed\u8d39\u8f6f\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("main", u"\u68c0\u6d4b\u5230\u65b0\u7248\u672c\u8bf7\u53bb\u5b98\u7f51\u4e0b\u8f7d\u6700\u65b0\u7248\u672c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("main", u"\u4e3b\u9875", None))
        self.checkBox_2.setText(QCoreApplication.translate("main", u"\u60ac\u6d6e\u7a97\u8ddf\u968f", None))
        self.checkBox.setText(QCoreApplication.translate("main", u"\u60ac\u6d6e\u64cd\u4f5c\u6761", None))
        self.checkBox_3.setText(QCoreApplication.translate("main", u"\u6253\u5f00\u81f3\u6258\u76d8", None))
        self.checkBox_4.setText(QCoreApplication.translate("main", u"\u5f00\u673a\u81ea\u542f\u52a8", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("main", u"ChatGpt", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("main", u"\u901a\u4e49\u5343\u95ee", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("main", u"\u6587\u5fc3\u4e00\u8a00", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("main", u"\u8baf\u98de\u661f\u706b", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("main", u"\u667a\u8c31\u6e05\u8a00", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("main", u"\u5b57\u8282\u8c46\u5305", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("main", u"deepseek", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("main", u"kimi", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("main", u"mytan", None))

        self.label.setText(QCoreApplication.translate("main", u"\u6a21\u578b\u9009\u62e9", None))
        self.pushButton.setText(QCoreApplication.translate("main", u"\u6253\u5f00Ai\u5b98\u7f51", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("main", u"\u8bbe\u7f6e", None))
    # retranslateUi

